import requests
import json

PLAYLIST_TO_BE_GENERATED_NAME = 'dev'

# Obtain an oauth token by going to https://developer.spotify.com/console/get-search-item/ and pressing "Get Token"
# Save this token in a file called oauthtoken.txt
with open('oauthtoken.txt') as f:
    token = f.readlines()[0].strip()
    bearer_token = f'Bearer {token}'

# Obtain Track IDs for each song track in the text file
# Obtain each song track in the text file
with open('songs.txt') as f:
    songs = f.readlines()
    songs = [song.strip() for song in songs]
# TODO remove
songs = songs[0:3]

# Query each song on Spotify Search API to get the Track ID
song_ids = []
search_endpoint_url = 'https://api.spotify.com/v1/search?'
limit = 1
market = 'US'
query_type = 'track'
spotify_user_id = 'shivkushwah'

for song in songs:
    search_query = f'{search_endpoint_url}q={song}&type={query_type}&limit={limit}&market={market}'
    response =requests.get(search_query,
                headers={"Content-Type":"application/json",
                            "Authorization":bearer_token})
    for item in response.json()['tracks']['items']:
        song_ids.append(item['id'])

# Create new playlist
playlist_endpoint_url = f'https://api.spotify.com/v1/users/{spotify_user_id}/playlists'
request_body = json.dumps({
          "name": PLAYLIST_TO_BE_GENERATED_NAME,
          "description": "dev time",
          "public": True
        })

response = requests.post(url = playlist_endpoint_url, data = request_body, headers={"Content-Type":"application/json",
                        "Authorization":bearer_token})
playlist_id = response.json()['id']
print(playlist_id)
