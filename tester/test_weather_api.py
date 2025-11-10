import requests


def test_api_check():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 59.33,
        "longitude": 18.06,
        "hourly": "temperature_2m",
        "timezone": "Europe/Stockholm",
    }

    response = requests.get(url, params=params)

    assert response.status_code == 200
