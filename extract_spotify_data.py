from fycharts.SpotifyCharts import SpotifyCharts
from pathlib import Path
import datetime
import logging
logging.basicConfig(level=logging.DEBUG)


filepath = Path("all_regions_top_200_weekly.csv")
regions = ["global", "uk", "us", "india", "spain", "canada"]

if not filepath.exists():
    api = SpotifyCharts()
    api.top200Weekly(output_file = str(filepath), start="2017-01-01", end="2021-01-01")
else:
    logging.debug(f"{datetime.datetime.now().replace(microsecond=0)}: No data downloaded.")
