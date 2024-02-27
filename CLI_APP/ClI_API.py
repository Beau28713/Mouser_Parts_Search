import requests


def scrape_and_save(part_data):
    url_redirect = "https://localhost"
    mouser_url = "https://api.mouser.com/api/v1/search/partnumber?apiKey=Enter API Key Here"
    response = requests.post(mouser_url, json=part_data)
    data = response.json()

    print(
        f"Part number searched: {part_data.get('SearchByPartRequest').get('mouserPartNumber')}\n"
    )
    print(f"Number of Results: {data['SearchResults']['NumberOfResult']}\n")
    print("Results: \n")

    for itm in data["SearchResults"]["Parts"]:
        if itm.get("Availability") == None:
            itm["Availability"] = "Not Available"
        print(f"Availability: {itm.get('Availability')}")
        print(f"Description: {itm.get('Description')}")
        print(f"DataSheet Url: {itm.get('DataSheetUrl')}")
        print(f"Lead time: {itm.get('LeadTime')}")
        print(f"Manufacturer: {itm.get('Manufacturer')}")
        print(f"Manufacturer PartNumber: {itm.get('ManufacturerPartNumber')}")
        print(f"Mouser PartNumber: {itm.get('MouserPartNumber')}")
        print(
            "-------------------------------------------------------------------------------------------------"
        )


# Example usage
part_data = {
    "SearchByPartRequest": {"mouserPartNumber": "2n2222a", "partSearchOptions": "None"}
}

scrape_and_save(part_data)
