import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

billboard_url = 'https://www.billboard.com/charts/hot-100'
date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
endpoint_url = f'{billboard_url}/2000-08-12'
spotify_client_id = '1f0749527fef416593ab7c30c604fa6c'
spotify_client_secret = 'd4d129f217734c1197dfb0f0757098f1'
example_domain = 'http://example.com/?code=AQCDmSbX2OtOYmKS_9K2oVTKFBR1FG6pdRe9CjWDfb9Hl0yTARUtY7u8W7Gydif6JtsRCQ903bxsP8-MOsTQLqOYx6UHfyDmwWUWmGJpRRI7Tnc64dhmRha6zUoZs4JujNRBocQUitNuz8bO8inMeq0G6NIDqw'
# some_token = '31raktac2hp3pufbavnnkivtwqsm'
response = requests.get(endpoint_url)
webpage_html = response.text
soup = BeautifulSoup(webpage_html, 'html.parser')
songs_titles = soup.select(selector='.o-chart-results-list__item h3')
song_names = [song.getText().strip() for song in songs_titles]
# print(songs_list)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username='Humoyun Oripov',
    )
)
user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
