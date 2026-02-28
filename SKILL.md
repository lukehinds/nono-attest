# Weather Skill

Get current weather information for a given location using the Google Weather API.

## Usage

Run the weather script with a location:

```bash
python scripts/call-weather.py --location "London"
```

## Requirements

- Python 3.8+
- `requests` library (`pip install requests`)
- A Google Maps API key set as the `GOOGLE_API_KEY` environment variable

## Parameters

| Parameter    | Required | Description                          |
|-------------|----------|--------------------------------------|
| `--location` | Yes      | City name or address to look up      |
| `--units`    | No       | `metric` (default) or `imperial`     |

## Examples

```bash
# Get weather in metric units
python scripts/call-weather.py --location "New York"

# Get weather in imperial units
python scripts/call-weather.py --location "Tokyo" --units imperial
```
