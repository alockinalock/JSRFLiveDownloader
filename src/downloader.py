import os
import time
import requests
from pathlib import Path

def download_station_urls(station_id, station_name, urls_file):
    base_path = Path(__file__).parent
    downloads_dir = base_path / "../downloads" / station_id
    failed_dir = base_path / "../data/failed_downloads"
    temp_dir = base_path / "../data/temp"


    downloads_dir.mkdir(parents=True, exist_ok=True)
    failed_dir.mkdir(parents=True, exist_ok=True)


    failed_file = failed_dir / f"{station_id}_failed_urls.txt"


    if failed_file.exists():
        failed_file.unlink()


    with open(urls_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]


    print(f"\n====================================================\n\nStarting downloads for station: {station_name}\n")
    for url in urls:
        filename = downloads_dir / Path(url).name
        print(f"Downloading: {url}")
        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            with open(filename, "wb") as out_file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        out_file.write(chunk)


            time.sleep(1)  # polite pause between downloads to reduce stress on server


        except requests.RequestException:
            print(f"Failed: {url}")
            with open(failed_file, "a", encoding="utf-8") as ff:
                ff.write(url + "\n")


    print(f"\n====================================================\n\nDownloads completed for station: {station_name}")
    print(f"Failed downloads (if any) are saved in: {failed_file}")


    print(f"\n====================================================\n\nCleaning temp files for station: {station_name}")
    temp_files = [
        temp_dir / f"{station_id}_raw.txt",
        temp_dir / f"{station_id}_urls.txt"
    ]


    for file_path in temp_files:
        if file_path.exists():
            file_path.unlink()
