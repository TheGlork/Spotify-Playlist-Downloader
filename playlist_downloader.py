import spotipy
from spotipy.oauth2 import SpotifyOAuth
from youtube_api import YouTubeDataAPI
from pytube import YouTube
import os
from moviepy.editor import VideoFileClip
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, YT_KEY, VIDEO_OUTPUT_PATH, AUDIO_OUTPUT_PATH

scope = "playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri='http://localhost:8888/callback', #needs to be same as the one given in your project in spotify
                                               scope=scope))

def get_playlist_tracks(playlist_url):
    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    print(f"Fetching tracks for playlist ID: {playlist_id}") 
    
    tracks = []
    
    try:
        # Fetch playlist tracks
        results = sp.playlist_tracks(playlist_id)
        if not results['items']:
            print("No tracks found in this playlist.")
            return []
        
        tracks.extend(results['items'])

        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])

        song_list = []
        for track in tracks:
            track_name = track['track']['name']
            artist_name = track['track']['artists'][0]['name']
            song_list.append(f"{track_name} by {artist_name}")

        return song_list
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error fetching playlist tracks: {e}")
        return []

def download_youtube_video(song):
    yt = YouTubeDataAPI(YT_KEY)

    searches = yt.search(q=song, max_results=5)
    if searches:
        video_id = searches[0]["video_id"]
        yt = YouTube('http://youtube.com/watch?v=' + video_id)

        print("Downloading video file: " + yt.title)
        print("Current Video ID: " + video_id)

        ind = yt.streams.filter(progressive=True)[0].itag
        stream = yt.streams.get_by_itag(ind)

        x = stream.download(output_path=VIDEO_OUTPUT_PATH, filename=song+".mp4")

        print("Video file has been downloaded.")
        print("Converting to audio file using FFmpeg and MoviePy.")
        
        video = VideoFileClip(os.path.join(VIDEO_OUTPUT_PATH, song + ".mp4"))
        video.audio.write_audiofile(os.path.join(AUDIO_OUTPUT_PATH, song + ".mp3"))
        
        print("Deleting video file.")
        os.remove(os.path.join(VIDEO_OUTPUT_PATH, song + ".mp4"))
        print("Download process has been completed.")
    else:
        print(f"No videos found for {song}")

playlist_url = 'YOUR COMPLETE SPOTIFY PLAYLIST URL' 
songs = get_playlist_tracks(playlist_url)

if songs:
    for song in songs:
        download_youtube_video(song)
else:
    print("No songs to download.")
