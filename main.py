from dotenv import load_dotenv
import os
import json
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from treeVisualizer import visualizeDict


class SpotipyObject:

    def __init__(self):
        self.spotifyObject = self.requestUserAuthorization()

    def requestUserAuthorization(self):
        load_dotenv()

        self.clientId = os.getenv("CLIENT_ID")
        self.clientSecret = os.getenv("CLIENT_SECRET")
        self.tuiClientId =  os.getenv("TUI_CLIENT_ID")
        self.tuiClientSecret = os.getenv("TUI_CLIENT_SECRET")

        self.scopes = ["user-read-currently-playing", "user-library-read"]
        self.scope = " ".join(self.scopes)

        spotifyObject = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope, client_id=self.clientId, client_secret=self.clientSecret, redirect_uri="http://localhost:8888/callback"))
        return spotifyObject


    def addScope(self,scope):
        self.scopes.append(scope)
        self.scope = " ".join(self.scopes)

    def deleteScope(self,scope):
        self.scopes.remove(scope)
        self.scope = " ".join(self.scopes)

    def printCurrentlyPlaying(self):
        self.currentlyPlaying = self.spotifyObject.currently_playing()
        self.currentArtist = module.currentlyPlaying['item']['artists'][0]['name']
        self.currentSong = module.currentlyPlaying['item']['name']
        print(f"{self.currentSong} - {self.currentArtist}")
        

    

    


module = SpotipyObject()
module.addScope("hola")
print(module.scope)
module.deleteScope("hola")
print(module.scope)
module.printCurrentlyPlaying()
print(visualizeDict(module.currentlyPlaying))

# currentlyPlaying = sp.current_user_playing_track()
# print(currentlyPlaying)
# print(type(currentlyPlaying))
# visualizeDict(currentlyPlaying)