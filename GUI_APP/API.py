from fastapi import FastAPI
import requests

from api_key import api_key
app = FastAPI()


@app.post("/search")
def search_parts(query: str):
    url = "https://api.mouser.com/api/v1/search/partnumber?"

    part_data = {
        "SearchByPartRequest": {"mouserPartNumber": query, "partSearchOptions": "None"}
    }

    params = {
        "apiKey": api_key,
    }
    response = requests.post(url, params=params, json=part_data)
    data = response.json()
    man_num = [
        {
            "ManufacturerPartNumber": part.get("ManufacturerPartNumber"),
            "MouserPartNumber": part.get("MouserPartNumber"),
            "Manufacturer": part.get("Manufacturer"),
            "Description": part.get("Description"),
            "DataSheetUrl": part.get("DataSheetUrl"),
            "Availability": part.get("Availability")
        }
        for part in data.get("SearchResults").get("Parts")
    ]
    return man_num
