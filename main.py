import requests

# Obtain an oauth token by going to https://developer.spotify.com/console/get-search-item/ and pressing "Get Token"

# Save this token in a file called oauthtoken.txt
with open('oauthtoken.txt') as f:
    token = f.readlines()[0].strip()

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

for song in songs:
    search_query = f'{search_endpoint_url}q={song}&type={query_type}&limit={limit}&market={market}'
    response =requests.get(search_query,
                headers={"Content-Type":"application/json",
                            "Authorization":f'Bearer {token}'})
    for item in response.json()['tracks']['items']:
        song_ids.append(item['id'])

print(song_ids)
