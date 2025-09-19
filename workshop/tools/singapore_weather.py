import httpx


PRIMARY_STATION = "S111"  # Scotts Road
FALLBACK_STATION = "S50"  # Clementi Road

API_ENDPOINTS = {
    "temperature": "https://api-open.data.gov.sg/v2/real-time/api/air-temperature",
    "humidity": "https://api-open.data.gov.sg/v2/real-time/api/relative-humidity",
    "rainfall": "https://api-open.data.gov.sg/v2/real-time/api/rainfall",
    "wind_speed": "https://api-open.data.gov.sg/v2/real-time/api/wind-speed"
}


def extract_station_data(response_data, stations):
    """
    Helper function to extract data from the first available station in the list.

    Args:
        response_data: API response data
        stations: List of station IDs to check in order of preference

    Returns: Value from the first available station, or None
    """
    if response_data.get("code") != 0:
        return None

    data = response_data.get("data", {})
    readings = data.get("readings", [])

    if not readings:
        return None

    reading = readings[0]
    station_reading = reading.get("data", [])

    reading_map = {r["stationId"]: r["value"] for r in station_reading}

    for station in stations:
        if station in reading_map:
            return reading_map[station]

    return None


def singapore_weather() -> str:
    """
    Returns Singapore weather information using NEA's API. For reference we are using weather station: S111: Scotts Road, failing which, we use S50: Clementi.
    1. Temperature: https://api-open.data.gov.sg/v2/real-time/api/air-temperature
    2. Relative humidity: https://api-open.data.gov.sg/v2/real-time/api/relative-humidity
    3. Rainfall: https://api-open.data.gov.sg/v2/real-time/api/rainfall
    4. Wind: https://api-open.data.gov.sg/v2/real-time/api/wind-speed
    """

    weather_data = {}
    stations = [PRIMARY_STATION, FALLBACK_STATION]

    with httpx.Client(timeout=10.0) as client:
        for metric, url in API_ENDPOINTS.items():
            try:
                response = client.get(url)
                response.raise_for_status()
                data = response.json()

                value = extract_station_data(data, stations)

                if metric == "temperature" and value is not None:
                    weather_data["temperature"] = f"{value}°C"
                elif metric == "humidity" and value is not None:
                    weather_data["humidity"] = f"{value}%"
                elif metric == "rainfall" and value is not None:
                    weather_data["rainfall"] = f"{value} mm"
                elif metric == "wind_speed" and value is not None:
                    weather_data["wind_speed"] = f"{value} km/h"

            except Exception as e:
                weather_data[metric] = "N/A"

    result = f"Weather in Singapore now:\n"
    result += f"Temperature: {weather_data.get('temperature', 'N/A')}\n"
    result += f"Humidity: {weather_data.get('humidity', 'N/A')}\n"
    result += f"Rainfall: {weather_data.get('rainfall', 'N/A')}\n"
    result += f"Wind Speed: {weather_data.get('wind_speed', 'N/A')}"

    return result
