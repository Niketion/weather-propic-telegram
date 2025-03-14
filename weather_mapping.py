def map_weather_code_to_icon(weather_code):
    """
    Maps the Open-Meteo weather code to an online high-resolution icon URL based on Icons8 (256x256).

    :param weather_code: Integer weather code from Open-Meteo.
    :return: URL string for the corresponding weather icon.
    """
    if weather_code == 0:
        # Clear sky
        icon_url = "https://img.icons8.com/color/256/sun.png"
    elif weather_code in [1, 2]:
        # Partly cloudy
        icon_url = "https://img.icons8.com/color/256/partly-cloudy-day.png"
    elif weather_code == 3:
        # Cloudy
        icon_url = "https://img.icons8.com/color/256/cloud.png"
    elif weather_code in [45, 48]:
        # Fog
        icon_url = "https://img.icons8.com/color/256/fog-day.png"
    elif weather_code in [51, 53, 55]:
        # Drizzle
        icon_url = "https://img.icons8.com/color/256/light-rain.png"
    elif weather_code in [56, 57]:
        # Freezing drizzle (using same as rain)
        icon_url = "https://img.icons8.com/color/256/rain.png"
    elif weather_code in [61, 63, 65]:
        # Rain
        icon_url = "https://img.icons8.com/color/256/rain.png"
    elif weather_code in [66, 67]:
        # Freezing rain (using same as rain)
        icon_url = "https://img.icons8.com/color/256/rain.png"
    elif weather_code in [71, 73, 75, 77]:
        # Snow
        icon_url = "https://img.icons8.com/color/256/snow.png"
    elif weather_code in [80, 81, 82]:
        # Showers
        icon_url = "https://img.icons8.com/color/256/rain.png"
    elif weather_code in [85, 86]:
        # Snow showers
        icon_url = "https://img.icons8.com/color/256/snow.png"
    elif weather_code in [95, 96, 99]:
        # Thunderstorm
        icon_url = "https://img.icons8.com/color/256/storm.png"
    else:
        # Default: Clear sky
        icon_url = "https://img.icons8.com/color/256/sun.png"
    
    return icon_url


if __name__ == "__main__":
    try:
        code = int(input("Enter the weather code: "))
        icon = map_weather_code_to_icon(code)
        print(f"For weather code {code}, the icon used is: {icon}")
    except ValueError:
        print("Please enter a valid integer for the weather code.")
