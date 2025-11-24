#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
json_to_csv.py
==============

Konvertiert das bereitgestellte JSON‑File in zwei CSV‑Dateien:
    * locations.csv  –  eine Zeile pro Location (eid = fid)
    * rooms.csv      –  eine Zeile pro Raum, verknüpft über die Spalte `fid`

Erweiterung:
    * Füge eine Spalte `sku` hinzu, wenn ein UUID v4 vorhanden ist.
    * Rooms: eigene `sku` je Raum + zusätzlich Feld `location` mit der Location‑SKU.
    * Locations: zusätzlich Feld `MeetingRoom` mit den zugehörigen Rooms‑SKUs.

Benutzung:
        python json_to_csv.py 2025-09-04_seminartool-data(2).json

Falls du das Skript ohne Parameter startest, wird nach einer Datei gefragt.
"""

import json
import sys
import uuid
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

import pandas as pd
from tqdm import tqdm


def flatten_contact(contact: Dict[str, Any]) -> Dict[str, Any]:
        """
        Die `contact`‑Struktur ist ein verschachteltes Dict.
        Wir holen die einzelnen Felder heraus und hängen sie an das
        übergeordnete Location‑Dict an.
        """
        if not isinstance(contact, dict):
                return {}
        # Präfix, damit klar ist, dass es sich um Kontaktdaten handelt
        return {f"contact_{k}": v for k, v in contact.items()}


def flatten_hotel(hotel: Dict[str, Any]) -> Dict[str, Any]:
        """Analog zu `flatten_contact`."""
        if not isinstance(hotel, dict):
                return {}
        return {f"hotel_{k}": v for k, v in hotel.items()}


def normalize_list_field(value: Any) -> str:
        """
        Viele Felder (z. B. `gastro`, `extras`) sind Listen.
        Für CSV wandeln wir sie in einen kommagetrennten String um.
        """
        if isinstance(value, list):
                return ", ".join(str(v) for v in value)
        return "" if value is None else str(value)


def is_uuid_v4_string(value: Any) -> bool:
        """Prüft, ob der Wert eine gültige UUID v4 ist."""
        try:
                u = uuid.UUID(str(value))
                return u.version == 4
        except (ValueError, TypeError, AttributeError):
                return False


def normalize_uuid_str(value: str) -> str:
        """Normalisiert eine UUID zu ihrer kanonischen (klein geschriebenen) Darstellung."""
        return str(uuid.UUID(str(value)))


def extract_uuid_v4_from_dict(d: Dict[str, Any]) -> Optional[str]:
        """
        Versucht, eine UUID v4 aus einem Dict zu extrahieren.
        Bevorzugt typische ID‑Felder, fällt sonst auf beliebige String‑Felder zurück.
        """
        if not isinstance(d, dict):
                return None

        preferred_keys = ("sku", "id", "uuid", "rid", "eid")
        for k in preferred_keys:
                if k in d and is_uuid_v4_string(d[k]):
                        return normalize_uuid_str(d[k])

        # Fallback: alle String‑Felder durchsuchen
        for v in d.values():
                if isinstance(v, str) and is_uuid_v4_string(v):
                        return normalize_uuid_str(v)

        return None

def toCsv(df: pd.DataFrame, filename: str, out_dir: Path = Path(".")):
        file_path = out_dir / filename
        df.to_csv(file_path, index=False, encoding="utf-8", quotechar='"', quoting=1)
        print(f"✅  {len(df)} Rows → {file_path}")

def load_json(path: Path) -> List[Dict[str, Any]]:
        """Lädt das JSON‑File und gibt die Liste von Locations zurück."""
        with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        if not isinstance(data, list):
                raise ValueError("Das JSON‑File muss ein Array von Objekten enthalten.")
        return data


def precompute_skus(
        raw_items: List[Dict[str, Any]]
) -> Tuple[Dict[Any, Optional[str]], Dict[Any, List[str]]]:
        """
        Erzeugt:
            - Mapping fid -> Location‑SKU (falls UUID v4 vorhanden, sonst None)
            - Mapping fid -> Liste der Room‑SKUs
        """
        loc_sku_by_fid: Dict[Any, Optional[str]] = {}
        room_skus_by_fid: Dict[Any, List[str]] = {}

        for item in raw_items:
                fid = item.get("fid")
                # Location‑SKU aus Location‑Objekt (oder explizit aus fid)
                loc_sku = extract_uuid_v4_from_dict(item)
                if not loc_sku and is_uuid_v4_string(fid):
                        loc_sku = normalize_uuid_str(fid)
                loc_sku_by_fid[fid] = loc_sku

                # Room‑SKUs sammeln
                room_skus: List[str] = []
                for room in item.get("rooms", []) or []:
                        r_sku = extract_uuid_v4_from_dict(room)
                        if r_sku:
                                room_skus.append(r_sku)
                room_skus_by_fid[fid] = room_skus
                
        dfRoomSkus = pd.DataFrame(room_skus_by_fid.items(), columns=["fid", "room_skus"])
                
        toCsv(dfRoomSkus, "room_skus_debug.csv")  # Debug-Ausgabe der Room-SKUs      
        return loc_sku_by_fid, room_skus_by_fid


def build_locations_df(
        raw_items: List[Dict[str, Any]],
        loc_sku_by_fid: Dict[Any, Optional[str]],
        room_skus_by_fid: Dict[Any, List[str]],
) -> pd.DataFrame:
        """
        Erstellt den DataFrame für `locations.csv`.
        Alle Felder des äußeren Objekts werden übernommen,
        Listen werden zu Strings konvertiert,
        verschachtelte Dicts (`contact`, `hotel`) werden abgeflacht.
        Zusätzlich:
            - `sku` (falls UUID v4 ermittelbar, sonst leer)
            - `MeetingRoom` (kommagetrennte Room‑SKUs)
        """
        rows = []
        for item in tqdm(raw_items, desc="Locations verarbeiten"):
                flat = {
                        k: normalize_list_field(v)
                        for k, v in item.items()
                        if k not in ("contact", "hotel", "rooms")
                }
                # Kontakt‑ und Hotel‑Daten hinzufügen
                flat.update(flatten_contact(item.get("contact", {})))
                flat.update(flatten_hotel(item.get("hotel", {})))

                fid = item.get("fid")
                meeting_rooms = ", ".join(room_skus_by_fid.get(fid, []))
                
                flat["MeetingRoom"] = meeting_rooms
                flat["containsPlace"] = meeting_rooms  # Alternativname für MeetingRoom

                rows.append(flat)
                
        df = pd.DataFrame(rows)

        dfLocation = pd.DataFrame(
                rows,
                columns=["fid", "MeetingRoom", "containsPlace"]
        )
        
        toCsv(dfLocation, "locations_debug.csv")  # Debug-Ausgabe der Rohdaten
        
        # Spaltenreihenfolge: fid, sku, danach der Rest
        if not df.empty:
                cols = ["fid", "sku"] + [c for c in df.columns if c not in ("fid", "sku")]
                df = df[cols]
        return df


def build_rooms_df(
        raw_items: List[Dict[str, Any]], loc_sku_by_fid: Dict[Any, Optional[str]]
) -> pd.DataFrame:
        """
        Erstellt den DataFrame für `rooms.csv`.
        Jede Zeile enthält die Felder eines Raumes plus die zugehörige `fid`.
        Zusätzlich:
            - `sku` je Raum (falls UUID v4 ermittelbar)
            - `location` = SKU der übergeordneten Location (falls vorhanden)
        """
        rows = []
        for item in tqdm(raw_items, desc="Rooms verarbeiten"):
                fid = item.get("fid")
                parent_sku = loc_sku_by_fid.get(fid) or ""
                for room in item.get("rooms", []) or []:
                        flat = {k: normalize_list_field(v) for k, v in room.items()}
                        flat["fid"] = fid
                        flat["sku"] = uuid.uuid4()
                        # explizit gefordert: Feld "location" mit der Location‑SKU
                        flat["containedInPlace"] = parent_sku
                        rows.append(flat)

        df = pd.DataFrame(rows,
                columns=["sku", "fid", "name", "containedInPlace"]
        )
        
        toCsv(df, "rooms_debug.csv")  # Debug-Ausgabe der Rohdaten
        
        # Spaltenreihenfolge: fid, location, sku, danach alphabetisch
        if not df.empty:
                fixed = ["fid", "containedInPlace", "sku"]
                rest = [c for c in df.columns if c not in fixed]
                df = df[fixed + rest]
        return df

def main(json_path: Path, out_dir: Path = Path(".")):
        raw = load_json(json_path)
        
        # Add uuid v4 SKUs to locations if not present
        for entry in raw:
             if 'sku' not in entry or not is_uuid_v4_string(entry['sku']):
                 entry['sku'] = str(uuid.uuid4())
                 
        toCsv(pd.DataFrame(raw), "locations_with_skus_debug.csv", out_dir)  # Debug-Ausgabe der Rohdaten mit SKUs

        # SKUs vorab berechnen (Location + Rooms)
        loc_sku_by_fid, room_skus_by_fid = precompute_skus(raw)

        # ---------- Locations ----------
        loc_df = build_locations_df(raw, loc_sku_by_fid, room_skus_by_fid)
        dfLocation = loc_df.assign(
                cms_fid=loc_df['fid'],
                name=loc_df.get('name', ''),
                disambiguatingDescription=loc_df.get('shortDescription', ''),
                description=loc_df.get('localityDescription', ''),
                MeetingRoomProducts=loc_df.get('MeetingRoom', ''),
                containsPlace=loc_df.get('containsPlace', ''),
        )
        dfLocation = dfLocation[['sku', 'cms_fid', 'name', 'MeetingRoomProducts', 'containsPlace']]
        
        toCsv(loc_df, "locationsOriginal.csv", out_dir)
        toCsv(dfLocation, "locations.csv", out_dir)
        
        # ---------- Rooms ----------
        rooms_df = build_rooms_df(raw, loc_sku_by_fid)
        dfRoom = rooms_df.assign(
                cms_fid=rooms_df['fid'],
                name=rooms_df.get('name', ''),
                containedInPlace=rooms_df.get('containedInPlace', ''),
        )
        dfRoom = dfRoom[['sku', 'cms_fid', 'name', 'containedInPlace']]
        
        toCsv(rooms_df, "roomsOriginal.csv", out_dir)
        toCsv(dfRoom, "rooms.csv", out_dir)

if __name__ == "__main__":
        # --------------------------------------------------------------
        # Argument‑Parsing (minimal, kein externes lib nötig)
        # --------------------------------------------------------------
        if len(sys.argv) >= 2:
                json_file = Path(sys.argv[1])
        else:
                json_file = Path("../../../input/atag/inputSeminarTool.json")
        if not json_file.is_file():
                sys.exit(f"❌  Datei nicht gefunden: {json_file}")

        # Optional: Ausgabe‑Ordner (Standard: aktuelles Verzeichnis)
        out_directory = Path("../../../input/atag/import/")
        main(json_file, out_directory)