# import requests
from weather_api_call import fetch_weather_data


def test_fetch_integration():

    df = fetch_weather_data()

    assert df is not None and not df.empty
