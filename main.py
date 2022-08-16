from urllib import response
from bs4 import BeautifulSoup
import requests

users_date = input('Which year do you want to travel to? \n Please type the date in the "YYYY-MM-DD" format: ')

response = requests.get("https://www.billboard.com/charts/hot-100/" + users_date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]
