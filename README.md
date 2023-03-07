# README

## Pre-req:
1. Clone this repo and cd to it
2. Obtain an oauth token by going to https://developer.spotify.com/console/get-search-item/ and pressing "Get Token”. Select all of the scopes.
3. `Touch oauthtoken.txt` and copy-paste the token in this file
4. In main.py, update PLAYLIST_TO_BE_GENERATED_NAME and PLAYLIST_TO_BE_GENERATED_DESCRIPTION to your specific values


## To run:
```
pip3 install requests
/usr/bin/python3 main.py
```

## Expected output
```
➜  spotify-text-to-playlist git:(main) ✗ /usr/bin/python3 main.py
Parsed songs from text file
Created new playlist with id 1kw8ERacNJ5pzKx5liIsdw
Finished adding songs to new playlist
Done!
```
