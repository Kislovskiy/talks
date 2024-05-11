import json

json_string = """{
    'head': {'vars': ['museum', 'museumLabel', 'location', 'locationLabel', 'subjectLabel', 'popularity']},
    'results': {
        'bindings': [
            {
                'museum': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q133982'},
                'museumLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Natural History Museum of Florence - Botany section'},
                'location': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q3963814'},
                'locationLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Società di studi geografici'},
                'subjectLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'botany'}
            }
        ]
    }
}"""

json_data = json.loads(json_string.replace("'", '"'))
print(json_data["results"]["bindings"][0]["museumLabel"]["value"])
museum_label = (
    json_data.get("results", {})
    .get("bindings", [{}])[0]
    .get("museumLabel", {})
    .get("value", None)
)
subject_label = (
    json_data.get("results", {})
    .get("bindings", [{}])[0]
    .get("subjectLabel", {})
    .get("value", None)
)
