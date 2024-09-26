# Spotify Playlist Downloader

Downloads all the songs of a given spotify playlist in mp3 format. Obtains the songs audio files from YouTube

## Setting Up config.py

Make a file in the same directory called config.py

```
SPOTIPY_CLIENT_ID = 'SPOTIFY CLIENT ID'
SPOTIPY_CLIENT_SECRET = 'SPOTIFY SECRET'
SPOTIPY_REDIRECT_URI = 'REDIRECT URI - SAME AS SPOTIFY ONE'  

YT_KEY = "YOUTUBE API KEY"

VIDEO_OUTPUT_PATH = "OUTPUT PATH FOR STORING VIDEO TEMPORARILY"
AUDIO_OUTPUT_PATH = "OUTPUT PATH FOR STORING AUDIO"
```

## Changing Output URI

Change the output URI in the code(line 13) to the one you entered while making your Spotify Project.

## Requirements
```
pip install pytube
pip install moviepy
pip install spotipy
```
1. Make sure to have FFmpeg installed on your PC (Required for conversion of MP4 to MP3)
2. Obtain Spotify CID, CS and YouTube API Key
3. YouTube API: https://console.cloud.google.com/marketplace/product/google/youtube.googleapis.com
4. Spotify CID and CS: https://developer.spotify.com/dashboard

## Using the script

1. Change the URL in line 74 to the Spotify Playlist that you want to download. 
2. Run the program. 
3. All the songs will be stored in the specified audio_files directory
