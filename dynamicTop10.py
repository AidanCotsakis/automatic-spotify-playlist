
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import requests
import time

clientID = "[ID]"
clientSecret = "[SECRET]"
redirectURI = "http://127.0.0.1:8080/"

scope = "user-library-read playlist-modify-public playlist-modify-private playlist-read-private"
username = "[USERNAME]"

dynamicName = "Dynamic Top 10"

artistIDs = [
"53XhwfbYqKCa1cC15pYq2q", #Imagine Dragons
"6eUKZXaKkcviH0Ku9w2n3V", #Ed Sheeran
"66CXWjxzNUsdJxJ2JdwvnR"  #Ariana Grande
]

token = SpotifyOAuth(scope = scope, username = username, client_id = clientID, client_secret = clientSecret, redirect_uri = redirectURI)
spotify = spotipy.Spotify(auth_manager = token)

# find playlist IDS
currentPlaylists = spotify.current_user_playlists()["items"]
for playlist in currentPlaylists:
	if playlist["name"] == dynamicName:
		dynamicID = playlist["id"]

# find URIs of top songs
songURIs = []
for artistID in artistIDs:
	topSongs = spotify.artist_top_tracks(artistID, country='CA')["tracks"]
	for song in topSongs:
		songURIs.append(song["uri"])

with open("dynamicURIs.txt", "r") as f:
	contents = f.read()

if len(contents) != 0:
	dynamicURIs = contents.split("\n")
else:
	dynamicURIs = []

dynamicCommonURIs = []

for URI in songURIs:
	if URI in dynamicURIs:
		dynamicCommonURIs.append(URI)

# remove unwated songs from dynamic playlist
removeURIs = []
for URI in dynamicURIs:
	if URI not in dynamicCommonURIs:
		removeURIs.append(URI)

if len(removeURIs) > 100:
	removeURIs = removeURIs[:100]
	print("REMOVAL LIMIT REACHED")

if len(removeURIs) != 0:
	spotify.playlist_remove_all_occurrences_of_items(dynamicID,removeURIs)

	dynamicURIs = [i for i in dynamicURIs if i not in removeURIs]

	with open("dynamicURIs.txt", "w") as f:
		f.write("\n".join(dynamicURIs))

# add unaccounted for songs to each playlist
addDynamicURI = []
for URI in songURIs:
	if URI not in dynamicCommonURIs:
		addDynamicURI.append(URI)

		dynamicURIs.append(URI)

if len(addDynamicURI) > 100:
	addDynamicURI = addDynamicURI[:100]
	print("ADDITION LIMIT REACHED")

if len(addDynamicURI) != 0:
	spotify.playlist_add_items(dynamicID, addDynamicURI)

	with open("dynamicURIs.txt", "w") as f:
		f.write("\n".join(dynamicURIs))

# notify user of changes made
if len(removeURIs) != 0:
	print("Removed the following URIs:")
	for URI in removeURIs:
		print(URI)

if len(addDynamicURI) != 0:
	print("Added the following URIs:")
	for URI in addDynamicURI:
		print(URI)

input("Done!")
