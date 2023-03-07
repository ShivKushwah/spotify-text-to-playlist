import requests
import json

PLAYLIST_TO_BE_GENERATED_NAME = '2016PLUS'
PLAYLIST_TO_BE_GENERATED_DESCRIPTION = 'Everything 2016 onwards'

# Obtain an oauth token by going to https://developer.spotify.com/console/get-search-item/ and pressing "Get Token"
# Save this token in a file called oauthtoken.txt
with open('oauthtoken.txt') as f:
    token = f.readlines()[0].strip()
    bearer_token = f'Bearer {token}'

# Obtain each song track in the text file
with open('songs.txt') as f:
    songs = f.readlines()
    songs = [song.strip() for song in songs]

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
    if (response.status_code >= 400):
        print("Spotify API Error: Couldn't find " + song)
        print(response.status_code)
        print(response.json())
        exit()
    try :
        for item in response.json()['tracks']['items']:
            song_ids.append('spotify:track:' + item['id'])
    except Exception as e:
        print("Skipping " + song)
print("Parsed songs from text file")

# Create new playlist
playlist_endpoint_url = f'https://api.spotify.com/v1/users/{spotify_user_id}/playlists'
request_body = json.dumps({
          "name": PLAYLIST_TO_BE_GENERATED_NAME,
          "description": PLAYLIST_TO_BE_GENERATED_DESCRIPTION,
          "public": True
        })
response = requests.post(url = playlist_endpoint_url, data = request_body, headers={"Content-Type":"application/json",
                        "Authorization":bearer_token})
if (response.status_code >= 400):
        print("Spotify API Error: Couldn't create playlist")
        print(response.status_code)
        print(response.json())
        exit()
playlist_id = response.json()['id']
print("Created new playlist with id " + playlist_id)

# Add songs to playlist in batches of 100
add_to_playlist_endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
for i in range(0, len(song_ids), 100):
    request_body = json.dumps({
            "uris" : song_ids[i:i+100]
            })
    response = requests.post(url = add_to_playlist_endpoint_url, data = request_body, headers={"Content-Type":"application/json",
                            "Authorization":bearer_token})
    if (response.status_code >= 400):
        print("Spotify API Error: Couldn't update playlist at index " + i)
        print(response.status_code)
        print(response.json())
        exit()

print("Finished adding songs to new playlist")
print("Done!")
