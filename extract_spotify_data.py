from fycharts.SpotifyCharts import SpotifyCharts
from pathlib import Path
import datetime
import logging
logging.basicConfig(level=logging.DEBUG)


filepath = Path("global_top_200_daily.csv")
regions = ["global"]

if not filepath.exists():
    api = SpotifyCharts()
    api.top200Daily(output_file = str(filepath), region = regions)
else:
    logging.debug(f"{datetime.datetime.now().replace(microsecond=0)}: No data downloaded.")
