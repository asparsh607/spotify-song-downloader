from pathlib import Path
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Loading environment variables
curr_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = curr_dir / ".env"
load_dotenv(envars)

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# connecting with spotify api
auth_manager = SpotifyClientCredentials(client_id,client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_song_list(playlist_link):
    song_list = []
    for count_of_songs in range(len(sp.playlist_tracks(playlist_link)["items"])):
        song_list.append(sp.playlist_tracks(playlist_link)["items"][count_of_songs]['track']['name'])
    return song_list