#
#       generate_links.py
#
#       Generates a .txt file containing a list of all urls to audio files on jetsetradiofuture.live by station
#
#       Note: Files downloaded via these links will be named in URL encoding (i.e. spaces as %20, etc.).
#

import re
import urllib.parse
import requests
from charset_normalizer import from_bytes
from pathlib import Path

temp_path = Path(__file__).parent / "../data/temp"

template_url = "https://jetsetradiofuture.live/radio/stations"

urls = []

def generate_urls(station):
        raw_temp_file = fetch_track_list(station['id'])
        if not raw_temp_file:
              print("Temp file not found. Either the program failed to generate it or it was moved/deleted. The program will now stop.")
              return


        extended_template_url = f"{template_url}/{station['id']}/"


        urls.clear()
        

        with open(raw_temp_file, "r", encoding="utf-8") as f:
                for line_number, line in enumerate(f, 1):
                        line = line.strip()
                        match = re.search(r'"(.+?)"', line)
                        if match:
                                track_name = match.group(1)
                                encoded_name = urllib.parse.quote(track_name)
                                url = f"{extended_template_url}/{encoded_name}.mp3"
                                urls.append(url)
                        else:
                                print(f"No match on line {line_number}: {line}")  # For debugging



        urls_temp_file = temp_path / f"{station['id']}_urls.txt"
        with open(urls_temp_file, "w", encoding="utf-8") as f:
              for url in urls:
                    f.write(url + "\n")

        print(f"\n====================================================\n\nGenerated {len(urls)} URLs.\nURL list temp file located at {urls_temp_file}")



def fetch_track_list(station):
    list_url = f"{template_url}/{station}/~list.js"
    try:
        response = requests.get(list_url)
        response.raise_for_status()
        js_content = response.text


        cleaned_js = "\n".join(js_content.splitlines()[13:])

        # Ensure temp folder exists
        temp_path.mkdir(parents=True, exist_ok=True)

        temp_file = temp_path / f"{station}_raw.txt"
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(cleaned_js)

        print(f"\n====================================================\n\nSuccessfully obtained raw track list.\nRaw track list temp file located at {temp_file}")

        return temp_file

    except requests.RequestException as e:
        print(f"Error encountered while fetching {station}: {e}")
        return ""