#
#       decoder.py
#
#       Cleans up the URL encoding created by generate_links.py
#


from pathlib import Path
import urllib.parse


def decode_songs(station_name):
        song_folder = Path(__file__).parent / "../downloads" / station_name


        if not song_folder.exists():
                print(f"Song folder missing for station id: {station_name}. Check path: {song_folder}")
                return
        

        print("\n====================================================\n")


        for file_path in song_folder.rglob("*.mp3"):
                decoded_name = urllib.parse.unquote(file_path.name).strip()
                new_path = file_path.with_name(decoded_name)


                if file_path != new_path:
                        if new_path.exists():
                                base, ext = new_path.stem, new_path.suffix
                                counter = 1
                                while True:
                                        candidate = file_path.with_name(f"{base}_{counter}{ext}")
                                        if not candidate.exists():
                                                new_path = candidate
                                                break
                                        counter += 1


                        print(f"Renaming: {file_path.name} → {new_path.name}")
                        file_path.rename(new_path)
        

        print(f"\nFinished decoding songs in {song_folder}\n\n====================================================")