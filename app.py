import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os
import sys
from dotenv import load_dotenv
from anytree import Node, RenderTree
load_dotenv()
n = len(sys.argv)
# 1st argument at index = 0 is app.py itself which is used to run the python script, so the artist names will start from index 1 to n-1
L = []
for i in range(1, n):
    L.append(sys.argv[i])
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET")
    )
)
for i in range(0, len(L)):
    artistName = L[i]
    main_Node = Node(artistName)
    results = sp.search(q=artistName)
    artist_url = results["tracks"]["items"][0]["album"]["artists"][0]["external_urls"][
        "spotify"
    ]
    artist_id = artist_url[32:]
    # We can add the limit to the number of it , should be displayed
    album_details = sp.artist_albums(artist_id, album_type="album")
    total_albums = len(album_details["items"])
    for i in range(1):
        album_name = album_details["items"][i]["name"]
        second_Node = Node(album_name,parent=main_Node)
        album_uri = album_details["items"][i]["uri"]
        track_details = sp.album_tracks(album_uri)
        total_tracks = len(track_details["items"])
        for j in range(0,total_tracks):
            track_name = track_details["items"][j]["name"]
            track_uri = track_details["items"][j]["uri"]
            third_Node = Node(track_name,parent=second_Node)
    for pre, fill, node in RenderTree(main_Node):
        print("%s%s" % (pre, node.name)+"\n")
