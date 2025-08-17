#
#       downloader.py
#
#       Uses temp files created by generate_links.py to send download requests for the mp3s.
#
#       Note: Files downloaded will be named in URL encoding (i.e. spaces as %20, etc.). This will be fixed with decoder.py
#

import os
import time
import requests
import shutil
from pathlib import Path

def download_station_urls(station_id, station_name, urls_file):
    base_path = Path(__file__).parent
    temp_downloads_dir = base_path / "../downloads/temp"
    final_downloads_dir = base_path / "../downloads" / station_name
    failed_dir = base_path / "../data/failed_downloads"
    temp_dir = base_path / "../data/temp"


    temp_downloads_dir.mkdir(parents=True, exist_ok=True)
    final_downloads_dir.mkdir(parents=True, exist_ok=True)
    failed_dir.mkdir(parents=True, exist_ok=True)


    failed_file = failed_dir / f"{station_name}_failed_urls.txt"


    if failed_file.exists():
        failed_file.unlink()


    with open(urls_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]


    print(f"\n====================================================\n\nStarting downloads for station: {station_name}\n")
    

    for url in urls:
        temp_filename = temp_downloads_dir / Path(url).name
        print(f"Downloading: {url}")
        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            with open(temp_filename, "wb") as out_file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        out_file.write(chunk)


            time.sleep(1)  # polite pause between downloads


        except requests.RequestException:
            print(f"Failed: {url}")
            with open(failed_file, "a", encoding="utf-8") as ff:
                ff.write(url + "\n")


    # Move files from temp to final folder
    for file_path in temp_downloads_dir.iterdir():
        target_path = final_downloads_dir / file_path.name
        shutil.move(str(file_path), str(target_path))


    shutil.rmtree(temp_downloads_dir)


    print(f"\n====================================================\n\nDownloads completed for station: {station_name}")
    print(f"Failed downloads (if any) are saved in: {failed_file}")


    print(f"\nCleaning temp files for station: {station_name}")
    temp_files = [
        temp_dir / f"{station_id}_raw.txt",
        temp_dir / f"{station_id}_urls.txt"
    ]


    for file_path in temp_files:
        if file_path.exists():
            file_path.unlink()
