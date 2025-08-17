#
#       main.py
#
#       Handles the user side of the program in console.
#

import generate_links
import downloader
from collections import defaultdict

def main():
    stations = [

        {"id": "brc", "name": "Bomb Rush Cyberfunk", "category": "New Stations"},
        {"id": "sonicrush", "name": "Sonic-Rush", "category": "New Stations"},
        {"id": "summer", "name": "Summer", "category": "New Stations"},
        {"id": "turntablism", "name": "Turntablism", "category": "New Stations"},
        {"id": "olliolliworld", "name": "Olliolli World", "category": "New Stations"},

        # Game OSTs
        {"id": "classic", "name": "Jet Set Radio Classic", "category": "Game OSTs"},
        {"id": "future", "name": "Jet Set Radio Future", "category": "Game OSTs"},


        {"id": "ggs", "name": "GG's", "category": "Gang / Ingame Themed Stations"},
        {"id": "noisetanks", "name": "Noise Tanks", "category": "Gang / Ingame Themed Stations"},
        {"id": "poisonjam", "name": "Poison Jam", "category": "Gang / Ingame Themed Stations"},
        {"id": "rapid99", "name": "Rapid 99", "category": "Gang / Ingame Themed Stations"},
        {"id": "loveshockers", "name": "Love Shockers", "category": "Gang / Ingame Themed Stations"},
        {"id": "immortals", "name": "The Immortals", "category": "Gang / Ingame Themed Stations"},
        {"id": "doomriders", "name": "Doom Riders", "category": "Gang / Ingame Themed Stations"},
        {"id": "goldenrhinos", "name": "Golden Rhinos", "category": "Gang / Ingame Themed Stations"},
        {"id": "garage", "name": "The Garage", "category": "Gang / Ingame Themed Stations"},


        {"id": "ganjah", "name": "Ganjah", "category": "Other"},
        {"id": "lofi", "name": "Lo-Fi", "category": "Other"},
        {"id": "classical", "name": "Classical Remix", "category": "Other"},
        {"id": "revolution", "name": "Revolution", "category": "Other"},
        {"id": "endofdays", "name": "End of Days", "category": "Other"},
        {"id": "chiptunes", "name": "Chiptunes", "category": "Other"},
        {"id": "retroremix", "name": "Retro Remix", "category": "Other"},
        {"id": "outerspace", "name": "Outer Space", "category": "Other"},


        {"id": "ultraremixes", "name": "Ultra Remixes", "category": "Mashups/Rips/Remixes"},
        {"id": "siivagunner", "name": "Silvagunner x JSR", "category": "Mashups/Rips/Remixes"},
        {"id": "jetmashradio", "name": "Jet Mash Radio", "category": "Mashups/Rips/Remixes"},


        {"id": "futuregeneration", "name": "Future Generation", "category": "Fan Albums"},
        {"id": "memoriesoftokyoto", "name": "Memories of Tokyo-To", "category": "Fan Albums"},
        {"id": "tokyotofuture", "name": "Sounds of Tokyo-To Future", "category": "Fan Albums"},
        {"id": "verafx", "name": "VeraFX", "category": "Fan Albums"},
        {"id": "djchidow", "name": "DJ Chidow", "category": "Fan Albums"},
        {"id": "bonafidebloom", "name": "BonafideBloom", "category": "Fan Albums"},


        {"id": "spacechannel5", "name": "Space Channel 5", "category": "Like-Minded Games"},
        {"id": "lethalleagueblaze", "name": "Lethal League Blaze", "category": "Like-Minded Games"},
        {"id": "hover", "name": "Hover", "category": "Like-Minded Games"},
        {"id": "butterflies", "name": "Butterflies", "category": "Like-Minded Games"},
        {"id": "ollieking", "name": "Ollie King", "category": "Like-Minded Games"},
        {"id": "crazytaxi", "name": "Crazy Taxi", "category": "Like-Minded Games"},
        {"id": "toejamandearl", "name": "Toe Jam & Earl", "category": "Like-Minded Games"},


        {"id": "halloween", "name": "Halloween", "category": "Seasonal"},
        {"id": "christmas", "name": "Christmas", "category": "Seasonal"},
        {"id": "snowfi", "name": "Snow-Fi", "category": "Seasonal"},
    ]

    stations_by_category = defaultdict(list)
    for station in stations:
        stations_by_category[station['category']].append(station)

    option_number = 1
    options_mapping = {}

    for category, station_list in stations_by_category.items():
        print(f"\n=== {category} ===")
        for station in station_list:
            print(f"{option_number}. {station['name']}")
            options_mapping[option_number] = station
            option_number += 1

    print("\n0. Quit")
    options_mapping[0] = None

    # user interaction
    while True:
        choice = input("\nSelect a station (enter a number): ")
        if not choice.isdigit():
            print("\nStation not found. Retry.")
            continue

        choice = int(choice)
        if choice not in options_mapping:
            print("\nStation not found. Retry.")
            continue

        if options_mapping[choice] is None:
            print("\nHalting process.")
            break

        selected_station = options_mapping[choice]
        print(f"\nYou selected: {selected_station['name']}")
        break

    # ===============================================================================================

    if 'selected_station' in locals():
        urls_temp_file_path = generate_links.generate_urls(selected_station)
        downloader.download_station_urls(selected_station['id'], selected_station['name'], urls_temp_file_path)


if __name__ == "__main__":
    main()
