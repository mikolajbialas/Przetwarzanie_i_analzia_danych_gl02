import requests
from typing import Union, List


class Brewery:
    def __init__(
        self,
        id_num: str,
        name: str,
        brewery_type: str,
        address_1: str,
        address_2: str,
        address_3: str,
        city: str,
        state_province: str,
        postal_code: str,
        country: str,
        longitude: float,
        latitude: float,
        phone: int,
        website_url: str,
        state: str,
        street: str,
    ):
        self.id = id_num
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self):
        final_string = (
            f"ID: {self.id}, Name: {self.name}, Brewery type: {self.brewery_type}, "
            f"Address_1: {self.address_1}, Address_2: {self.address_2}, Address_3: {self.address_3},"
            f"City: {self.city}, State Province: {self.state_province}, Postal Code: {self.postal_code},"
            f"Country: {self.country}, Longitude : {self.longitude}, Latitude: {self.latitude},"
            f" Phone: {self.phone}, Website URL: {self.website_url}, State: {self.state},"
            f" Street: {self.street}"
        )
        return final_string


def get_breweries(city: str = None) -> Union[List, None]:
    response = requests.get("https://api.openbrewerydb.org/v1/breweries")

    if response.status_code == 200:
        data = response.json()
        breweries = []

        for i in range(20):
            brewery_data = data[i]
            brewery_instance = Brewery(
                brewery_data["id"],
                brewery_data["name"],
                brewery_data["brewery_type"],
                brewery_data["address_1"],
                brewery_data["address_2"],
                brewery_data["address_3"],
                brewery_data["city"],
                brewery_data["state_province"],
                brewery_data["postal_code"],
                brewery_data["country"],
                brewery_data["longitude"],
                brewery_data["latitude"],
                brewery_data["phone"],
                brewery_data["website_url"],
                brewery_data["state"],
                brewery_data["street"],
            )
            breweries.append(brewery_instance)

        return breweries
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


def main():
    breweries = get_breweries()

    for brewer in breweries:
        print(brewer)


if __name__ == "__main__":
    main()
