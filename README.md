# JSRFLiveDownloader
Downloads the audio files from the jetsetradiofuture.live website.

### Features
* Downloads all tracks for a particular station from jetsetradiofuture.live
* Decodes file names to remove URL encoding automatically

### Dependencies

* Python/Python3
* pip/pip3

### How to use

1. Clone this repository
```
git clone https://github.com/alockinalock/JSRFLiveDownloader.git
``` 

2. Install Python dependencies
```
pip install -r requirements.txt
``` 
>Users may need to use pip3 instead of pip.

3. Run main.py
```
python main.py
``` 
>Users may need to use python3 instead of python.

### Output

Files are downloaded in mp3 format with varying bit rates

Downloaded files will be located in the downloads folder, subfolders are named based on station names.

### Planned updates

- Fixing missing metadata for artist and song title using mutagen (optional)
- Creating a .csv/.txt for metadata of all songs in a particular station (default)


