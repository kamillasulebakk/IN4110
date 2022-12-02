#!/usr/bin/env python3
"""
Fetch data from https://www.hvakosterstrommen.no/strompris-api
and visualize it.

Assignment 5
"""

import datetime

import altair as alt
import pandas as pd
import requests
import requests_cache
import json


# install an HTTP request cache
# to avoid unnecessary repeat requests for the same data
# this will create the file http_cache.sqlite
requests_cache.install_cache()

# task 5.1:


def fetch_day_prices(date: datetime.date = datetime.date.today(), location: str = "NO1") -> pd.DataFrame:
    """Fetch one day of data for one location from hvakosterstrommen.no API

    Arguments:
        date (datetime.date object) : the date to fetch prices from
        location (str) : the location code,
            starting with "NO", then a number 1-5

    Returns:
        df (DataFrame) : pandas DataFrame containing the electricity prices
            with columns: NOK_per_kWh (float) and time_start (datetime)
    """

    assert date >= datetime.date(2022, 10, 2), 'date must be after the 2nd of October 2022'

    date = str(date).split("-")

    url = f"https://www.hvakosterstrommen.no/api/v1/prices/{date[0]}/{date[1]}-{date[2]}_{location}.json"
    response = requests.get(url, verify=False)
    html_str = response.text

    data = json.loads(html_str)

    desired_columns = ["NOK_per_kWh", "time_start"]

    df = pd.DataFrame(data, columns=desired_columns)

    # fixing the issue with crossing Daylight Savings Time on 10/29
    df["time_start"] = pd.to_datetime(df["time_start"], utc=True).dt.tz_convert("Europe/Oslo")

    return df


# LOCATION_CODES maps codes ("NO1") to names ("Oslo")
LOCATION_CODES = {
    "NO1": "Oslo",
    "NO2": "Kristiansand",
    "NO3": "Trondheim",
    "NO4": "Tromsø",
    "NO5": "Bergen"
}

# task 1:

def fetch_prices(
    end_date: datetime.date = datetime.date.today(),
    days: int = 7,
    locations=tuple(LOCATION_CODES.keys()),
) -> pd.DataFrame:
    """Fetch prices for multiple days and locations into a single DataFrame

    Arguments:
        end_date (datetime.date object) : the end date to fetch prices from
        days (int) : the amont of days to fetch up to and including end_date
        locations (tuple) : all desired location codes

    Returns:
        df (DataFrame) : pandas DataFrame containing the electricity prices
            with columns: NOK_per_kWh (float), time_start (datetime),
            location code (str) and location name (str)
    """

    df = pd.DataFrame()
    desired_columns = ["NOK_per_kWh", "time_start", "location_code", "location"]


    # the date to start fetching from
    date = end_date - datetime.timedelta(days=days-1)

    for day in range(days):
        date_str = str(date).split("-")
        for location in locations:
            url = f"https://www.hvakosterstrommen.no/api/v1/prices/{date_str[0]}/{date_str[1]}-{date_str[2]}_{location}.json"
            response = requests.get(url, verify=False)
            html_str = response.text

            data = json.loads(html_str)

            # add desired columns to data
            for element in data:
                element["location_code"] = location
                element["location"] = LOCATION_CODES[location]

            temp = pd.DataFrame(data, columns=desired_columns)

            # copy temp into final data frame for every day and location
            df = pd.concat([df, temp])

        date += datetime.timedelta(days=1)

    # fixing the issue with crossing Daylight Savings Time on 10/29
    df["time_start"] = pd.to_datetime(df["time_start"], utc=True).dt.tz_convert("Europe/Oslo")

    return df

# task 5.1:


def plot_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot energy prices over time

    x-axis is time_start
    y-axis is price in NOK
    each location has its own line

    Arguments:
        df (DataFrame) : DataFrame containing data to plot
    """

    img = alt.Chart(df).mark_line().encode(
        alt.X("time_start"),
        alt.Y("NOK_per_kWh"),
        alt.Color('location')
    )

    return img



# Task 5.4


def plot_daily_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot the daily average price

    x-axis should be time_start (day resolution)
    y-axis should be price in NOK

    You may use any mark.

    Make sure to document arguments and return value...
    """
    ...


# Task 5.6

ACTIVITIES = {
    # activity name: energy cost in kW
    ...
}


def plot_activity_prices(
    df: pd.DataFrame, activity: str = "shower", minutes: float = 10
) -> alt.Chart:
    """
    Plot price for one activity by name,
    given a data frame of prices, and its duration in minutes.

    Make sure to document arguments and return value...
    """

    ...

def test_fetch_prices():
    date = datetime.date(2022, 11, 5)
    location = "NO1"
    df_day = fetch_day_prices(date)
    df = fetch_prices(end_date=date, days=1, locations=[location])
    assert "location" in df.columns
    assert "location_code" in df.columns
    assert (df["location"] == "Oslo").all()
    assert (df["location_code"] == "NO1").all()
    print(df["time_start"])
    print(df_day["time_start"])
    assert (df["time_start"] == df_day["time_start"]).all()


def main():
    """Allow running this module as a script for testing."""
    test_fetch_prices()
    input()
    df = fetch_day_prices()
    df = fetch_prices()
    chart = plot_prices(df)
    # showing the chart without requiring jupyter notebook or vs code for example
    # requires altair viewer: `pip install altair_viewer`
    chart.show()




if __name__ == "__main__":
    main()
