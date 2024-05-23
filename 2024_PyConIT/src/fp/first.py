# Get the number of museums in Florence from Wikipedia
# broupBy type

# Get museums in Florence from Wikidata
#
# PREFIX wd: <http://www.wikidata.org/entity/>
# PREFIX wdt: <http://www.wikidata.org/prop/direct/>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX schema: <http://schema.org/>
# SELECT DISTINCT ?museum ?museumLabel ?location ?locationLabel ?subjectLabel ?popularity WHERE {
#   ?museum wdt:P31 wd:Q33506;           # Instance of museum
#           wdt:P131 wd:Q2044;           # Located in Florence
#           rdfs:label ?museumLabel.
#   FILTER(LANG(?museumLabel) = "en").

#   ?location wdt:P131* wd:Q2044;        # Location is Florence
#             rdfs:label ?locationLabel.
#   FILTER(LANG(?locationLabel) = "en").

#   OPTIONAL {
#     ?museum wdt:P921 ?subject.
#     ?subject rdfs:label ?subjectLabel.
#     FILTER(LANG(?subjectLabel) = "en").
#   }

#   OPTIONAL {
#     ?museum wdt:P813 ?date.
#     ?museum wikibase:pageviews ?popularity.
#   }
# } LIMIT 300


def double(x: int) -> int:
    return x * 2
