from dotenv import load_dotenv
import os
import json
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from treeVisualizer import visualizeDict


class SpotipyObject:

    def __init__(self):
        self.requestUserAuthorization()

    def requestUserAuthorization(self):
        load_dotenv()

        self.clientId = os.getenv("CLIENT_ID")
        self.clientSecret = os.getenv("CLIENT_SECRET")
        self.tuiClientId =  os.getenv("TUI_CLIENT_ID")
        self.tuiClientSecret = os.getenv("TUI_CLIENT_SECRET")

        self.scopes = ["user-read-currently-playing", "user-library-read"]
        self.scope = " ".join(self.scopes)

        self.spotifyObject = spotipy.Spotify(auth_manager=SpotifyOAuth( 
            scope=self.scope, client_id=self.clientId, client_secret=self.clientSecret, redirect_uri="http://localhost:8888/callback", 
            cache_path='/home/jani/Projects/SpotifyListener/.cache-tkogds@gmail.com'))
        return


    def addScope(self,scope):
        self.scopes.append(scope)
        self.scope = " ".join(self.scopes)

    def deleteScope(self,scope):
        self.scopes.remove(scope)
        self.scope = " ".join(self.scopes)

    def printCurrentlyPlaying(self):
        self.currentlyPlaying = self.spotifyObject.currently_playing()
        if self.currentlyPlaying == None: return
        self.currentArtist = self.currentlyPlaying['item']['artists'][0]['name']
        self.currentSong = self.currentlyPlaying['item']['name']
        print(f"{self.currentSong} - {self.currentArtist}")
    
