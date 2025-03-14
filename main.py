import requests
import asyncio
import tempfile
import yaml
from geolocation import get_coordinates
from weather_mapping import map_weather_code_to_icon
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import nest_asyncio
import logging

nest_asyncio.apply()

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

API_ID = config['api_id']
API_HASH = config['api_hash']
SESSION_NAME = config['telegram_session_name']
TELEGRAM_PHONE = config['telegram_phone']
TELEGRAM_PASSWORD = config['telegram_password']

# Initialize the Telegram client using configuration from the YAML file
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def safe_connect(client, timeout=10):
    """
    Attempts to connect to the Telegram client with a specified timeout.

    :param client: TelegramClient instance.
    :param timeout: Maximum time in seconds to wait for connection.
    :return: True if connection was successful, False otherwise.
    """
    try:
        await asyncio.wait_for(client.connect(), timeout)
    except asyncio.TimeoutError:
        print("Timeout: Unable to connect within the specified time.")
        return False
    return True

async def update_profile_pic(image_url):
    """
    Downloads an image from the given URL and updates the Telegram profile picture.
    Handles user authentication if not already authorized.

    :param image_url: URL of the image to use as profile photo.
    """
    # Download image from URL
    response = requests.get(image_url)
    if response.status_code != 200:
        print("Error downloading image.")
        return
    
    # Save the downloaded image to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
        tmp_file.write(response.content)
        tmp_file_path = tmp_file.name

    # Connect to Telegram
    await client.connect()
    if not await client.is_user_authorized():
        # Send authentication code request
        await client.send_code_request(TELEGRAM_PHONE)
        code = input("Enter the code you received: ")
        try:
            await client.sign_in(TELEGRAM_PHONE, code)
        except SessionPasswordNeededError:
            # If two-step verification is enabled, sign in with the password
            await client.sign_in(password=TELEGRAM_PASSWORD)
    
    # Upload the file and update the profile photo
    photo = await client.upload_file(tmp_file_path)
    await client(UploadProfilePhotoRequest(file=photo))
    await client.disconnect()

def get_weather_code(latitude, longitude):
    """
    Retrieves the current weather code from the Open-Meteo API.

    :param latitude: Latitude coordinate.
    :param longitude: Longitude coordinate.
    :return: Weather code as an integer.
    """
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(weather_url)
    data = response.json()
    return data["current_weather"]["weathercode"]

def main():
    """
    Main function:
    1. Prompts the user for a city name.
    2. Retrieves the coordinates of the city.
    3. Gets the current weather code.
    4. Maps the weather code to a high-resolution icon URL.
    5. Updates the Telegram profile picture using the selected icon.
    """
    city = input("Enter the city name: ")
    try:
        lat, lon = get_coordinates(city)
        print(f"Coordinates for {city}: Latitude = {lat}, Longitude = {lon}")
    except ValueError as e:
        print(e)
        return
    
    code = get_weather_code(lat, lon)
    print(f"Weather code obtained: {code}")
    icon_url = map_weather_code_to_icon(code)
    print(f"Selected icon URL: {icon_url}")
    
    # Update the Telegram profile picture with the downloaded icon
    asyncio.run(update_profile_pic(icon_url))

if __name__ == "__main__":
    main()
