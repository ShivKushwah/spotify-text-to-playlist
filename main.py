# Obtain an oauth token by going to https://developer.spotify.com/console/get-search-item/ and pressing "Get Token"
# Save this token in a file called oauthtoken.txt
with open('oauthtoken.txt') as f:
    token = f.readlines()[0]
print(token)
