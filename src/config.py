ignoreTypes = [
    "schema:AskPublicNewsArticle", 
    "schema:UseAction", 
    "schema:FollowAction", 
    "schema:InteractionCounter",
    "schema:LodgingBusiness",
    "schema:Action",
    "schema:BioChemEntity",
    "schema:CreativeWork",
    "schema:Intangible",
    "schema:MedicalEntity",
    "schema:Patient",
    "schema:Taxon",
    "schema:3DModel",
    "schema:AboutPage",
    "schema:AcceptAction",
    ]

ignoreProperties = [
    "schema:alternateName",
]

mappingProperties = {
    "schema:additionalType": "schema:URL",
}

schemaorgURL = "https://schema.org/version/latest/schemaorg-current-https.jsonld"
