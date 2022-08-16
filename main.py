from urllib import response
from bs4 import BeautifulSoup
import requests
from dontlook import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth

JT_SPOTIFY_ID = jt_spotify_ID
JT_SPOTIFY_SECRET = jt_spotify_secret

# Scrapes the Billbaord 100
users_date = input('Which year do you want to travel to? \n Please type the date in the "YYYY-MM-DD" format: ')

response = requests.get("https://www.billboard.com/charts/hot-100/" + users_date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=jt_spotify_ID,
        client_secret=jt_spotify_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = users_date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song}year:{year}",type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")

# Creating a new private playlist for Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{users_date} Billboard 100", public=False)
print(playlist)

# Adding songs from found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)