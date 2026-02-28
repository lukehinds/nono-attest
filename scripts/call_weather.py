#!/usr/bin/env python3
"""Fetch current weather for a location using Google Maps and Weather APIs."""

import argparse
import json
import os
import sys

import requests

GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
WEATHER_URL = "https://weather.googleapis.com/v1/currentConditions:lookup"


def get_coordinates(location: str, api_key: str) -> tuple[float, float]:
    """Geocode a location string to latitude and longitude."""
    resp = requests.get(
        GEOCODE_URL,
        params={"address": location, "key": api_key},
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()
    if data["status"] != "OK" or not data.get("results"):
        print(f"Error: Could not geocode location '{location}'", file=sys.stderr)
        sys.exit(1)
    geo = data["results"][0]["geometry"]["location"]
    return geo["lat"], geo["lng"]


def get_weather(lat: float, lng: float, api_key: str, units: str) -> dict:
    """Fetch current weather conditions for given coordinates."""
    resp = requests.get(
        WEATHER_URL,
        params={
            "key": api_key,
            "location.latitude": lat,
            "location.longitude": lng,
            "unitsSystem": units.upper(),
        },
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()


def main():
    parser = argparse.ArgumentParser(description="Get weather for a location")
    parser.add_argument("--location", required=True, help="City or address")
    parser.add_argument(
        "--units",
        choices=["metric", "imperial"],
        default="metric",
        help="Unit system (default: metric)",
    )
    args = parser.parse_args()

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable is not set", file=sys.stderr)
        sys.exit(1)

    lat, lng = get_coordinates(args.location, api_key)
    weather = get_weather(lat, lng, api_key, args.units)
    print(json.dumps(weather, indent=2))


if __name__ == "__main__":
    main()
