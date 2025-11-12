import pandas as pd
from datetime import datetime, timedelta
from weather_api_call import fetch_weather_data, process_weather_data


def test_fetch_integration():

    df = fetch_weather_data()

    # Check that the function did not return None (no KeyError, TimeOut, etc.)
    assert df is not None

    # Check that the DataFrame is not empty
    assert not df.empty


def test_process_data_returns_24_hours():

    # Creating the "fake" data
    now = datetime.now()
    fake_times = [
        now - timedelta(hours=1),  # already past
        now + timedelta(minutes=30),  # should be included
        now + timedelta(hours=12),  # should be included
        now + timedelta(hours=48),  # more than 24 hours in future
    ]
    fake_temps = [5.0, 10.0, 15.0, 20.0]
    fake_df = pd.DataFrame(data={"time": fake_times, "temperature": fake_temps})

    result_df = process_weather_data(fake_df)

    # Chek that the function filtered exactly 24 hours of data
    assert len(result_df) == 2

    # Check that the 'temperature' column exists
    assert "temperature" in result_df.columns

    # Check that the data in 'temperature' is a number
    assert pd.api.types.is_numeric_dtype(result_df["temperature"])
