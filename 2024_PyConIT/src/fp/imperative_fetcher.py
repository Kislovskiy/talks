import requests
import json
from rich import print as rprint


def get_florence_museums() -> dict:
    sparql_query = """
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX schema: <http://schema.org/>

    SELECT DISTINCT ?museum ?museumLabel ?location ?locationLabel ?subjectLabel ?popularity WHERE {
    ?museum wdt:P31 wd:Q33506;           # Instance of museum
            wdt:P131 wd:Q2044;           # Located in Florence
            rdfs:label ?museumLabel.
    FILTER(LANG(?museumLabel) = "en").

    ?location wdt:P131* wd:Q2044;        # Location is Florence
                rdfs:label ?locationLabel.
    FILTER(LANG(?locationLabel) = "en").

    OPTIONAL {
        ?museum wdt:P921 ?subject.
        ?subject rdfs:label ?subjectLabel.
        FILTER(LANG(?subjectLabel) = "en").
    }
    } LIMIT 500
    """

    sparql_endpoint = "https://query.wikidata.org/sparql"

    headers = {"User-Agent": "Simple Wikidata SPARQL Client (Python Requests)"}

    params = {"query": sparql_query, "format": "json"}

    response = requests.get(sparql_endpoint, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return dict()


if __name__ == "__main__":
    museums_data = get_florence_museums()
    museums = []
    for result in museums_data.get("results", {}).get("bindings", []):
        museum = {
            "museum": result.get("museumLabel", {}).get("value", None),
            "location": result.get("locationLabel", {}).get("value", None),
            "subject": result.get("subjectLabel", {}).get("value", None),
        }
        museums.append(museum)
    rprint(museums)
    print(len(museums))
