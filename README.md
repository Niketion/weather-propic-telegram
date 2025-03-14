# Telegram Weather Profile Picture Updater

This project automatically updates your Telegram profile picture based on the current weather conditions in a specified city. It uses the Open-Meteo API for weather data, retrieves city coordinates via the Open-Meteo geocoding API, maps weather codes to high-resolution weather icons (from Icons8), and then updates your Telegram profile picture using Telethon.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Features

- **Weather Data Retrieval:** Fetches the current weather code from the Open-Meteo API.
- **Icon Mapping:** Maps the weather code to a high-resolution (256x256) weather icon from Icons8.
- **City Geocoding:** Retrieves the latitude and longitude of a given city using Open-Meteo's geocoding API.
- **Telegram Profile Update:** Downloads the corresponding weather icon and updates your Telegram profile picture.
- **Secure Configuration:** Sensitive credentials and settings are stored in a separate YAML configuration file.

---

## Project Structure

```
.
├── config.yaml           # Contains Telegram API credentials and user settings
├── geolocation.py        # Retrieves city coordinates using Open-Meteo's geocoding API
├── main.py               # Main script integrating all functionalities
├── weather_mapping.py    # Maps weather codes to high-resolution icon URLs
└── README.md             # Project documentation
```

---

## Prerequisites

- **Python 3.7+**

**Required Libraries:**
- `requests`
- `telethon`
- `pyyaml`
- `nest_asyncio`

Install the dependencies using pip:

```bash
pip install requests telethon pyyaml nest_asyncio
```

---

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Create and Configure `config.yaml`:**

   Create a file named `config.yaml` in the project root with the following content. Replace the placeholder values with your actual credentials:

   ```yaml
   # config.yaml
   api_id: "your_api_id_here"
   api_hash: "your_api_hash_here"
   telegram_session_name: "your_session_name_here"
   telegram_phone: "+1234567890"
   telegram_password: "your_2fa_password_here"
   ```

   > **Note:** You can obtain your `api_id` and `api_hash` by registering an app at [my.telegram.org](https://my.telegram.org).

---

## Usage

Run the main script with Python:

```bash
python main.py
```

**Workflow:**

1. **City Input:** The script prompts you to enter a city name.
2. **Geocoding:** It retrieves the city's latitude and longitude via the Open-Meteo geocoding API.
3. **Weather Data:** The current weather code is fetched from the Open-Meteo API.
4. **Icon Mapping:** The weather code is mapped to a high-resolution icon URL.
5. **Profile Update:** The icon is downloaded and used to update your Telegram profile picture.

---

## Troubleshooting

- **Connection Issues:**  
  Ensure your network is stable and not blocking access to Telegram or the required API endpoints.

- **Invalid Credentials:**  
  Double-check the values in `config.yaml` for correctness.

- **Two-Step Verification:**  
  If your Telegram account has two-step verification enabled, the script will prompt you for your Telegram password after you enter the authentication code.

- **Dependencies:**  
  Verify that all required Python packages (`requests`, `telethon`, `pyyaml`, `nest_asyncio`) are installed.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- [Open-Meteo API](https://open-meteo.com/)
- [Icons8](https://icons8.com/)
- [Telethon](https://docs.telethon.dev/)

