import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os
import sys
from dotenv import load_dotenv

load_dotenv()
n = len(sys.argv)
# 1st argument at index = 0 is app.py itself which is used to run the python script, so the artist names will start from index 1 to n-1
L = []
for i in range(1, n):
    L.append(sys.argv[i])
print(L)
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET")
    )
)
