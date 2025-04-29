import requests
from pprint import pprint
from config import OS_API_KEY
if not OS_API_KEY:
    raise ValueError("The OS_API_KEY environment variable is not set")

def pepCheck(name, dob):
    headers = {
        "Authorization": OS_API_KEY,
    }
    query = {
        "queries": {
            "q1": {
                "schema": "Person",
                "properties": {"name": name, "birthDate": dob},
            }
        }
    }
    response = requests.post(
        "https://api.opensanctions.org/match/peps", headers=headers, json=query
    )
    response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
    
    results = []
    for result in response.json()["responses"]["q1"]["results"]:
        if(result["match"] == False):
            continue
        results.append(
            {
                "id": result["id"],
                "name": result["caption"],
                "match": result["match"],
                "score": result["score"],
            }
        )
    return results
    
    
    
        
