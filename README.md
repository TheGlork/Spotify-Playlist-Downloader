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
