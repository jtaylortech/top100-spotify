from urllib import response
from bs4 import BeautifulSoup
import requests
from dontlook import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth

JT_SPOTIFY_ID = jt_spotify_ID
JT_SPOTIFY_SECRET = jt_spotify_secret

users_date = input('Which year do you want to travel to? \n Please type the date in the "YYYY-MM-DD" format: ')

response = requests.get("https://www.billboard.com/charts/hot-100/" + users_date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

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