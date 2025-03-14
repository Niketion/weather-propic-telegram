import requests

def get_coordinates(city_name):
    """
    Retrieves the latitude and longitude of the specified city using the Open-Meteo geocoding API.

    :param city_name: Name of the city.
    :return: Tuple of (latitude, longitude).
    :raises ValueError: If no results are found for the given city.
    """
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}"
    response = requests.get(url)
    data = response.json()
    if "results" in data and data["results"]:
        result = data["results"][0]
        latitude = result["latitude"]
        longitude = result["longitude"]
        return latitude, longitude
    else:
        raise ValueError(f"No results found for city: {city_name}")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    try:
        lat, lon = get_coordinates(city)
        print(f"Coordinates for {city}: Latitude = {lat}, Longitude = {lon}")
    except ValueError as e:
        print(e)
