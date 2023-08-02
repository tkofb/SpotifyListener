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

        
        

    def addScope(self,scope):
        self.scopes.append(scope)
        self.scope = " ".join(self.scopes)
        self.requestUserAuthorization()

    def deleteScope(self,scope):
        self.scopes.remove(scope)
        self.scope = " ".join(self.scopes)
        self.requestUserAuthorization()


    def printCurrentlyPlaying(self):
        if self.songPlaying():
            self.currentArtist = self.currentlyPlaying['item']['artists'][0]['name']
            self.currentSong = self.currentlyPlaying['item']['name']
            print(f"{self.currentSong} - {self.currentArtist}")
        else:
            print("jani")


    def songPlaying(self):
        self.currentlyPlaying = self.spotifyObject.currently_playing()
            
        if self.currentlyPlaying == None: 
            return False

        if self.currentlyPlaying["currently_playing_type"] != 'track': 
            return False
        
        return True

    def nextSong(self):
        if self.songPlaying():
            necessaryScope = "user-modify-playback-state"
            if necessaryScope not in self.scopes:
                self.addScope(necessaryScope)
                
            self.spotifyObject.next_track()
        
    def toggleShuffle(self):
        if self.songPlaying():
            necessaryScope = "user-modify-playback-state"
            if necessaryScope not in self.scopes:
                self.addScope(necessaryScope)
                
            self.spotifyObject.shuffle(True)

    def pauseSong(self):
        if self.songPlaying():
            necessaryScope = "user-modify-playback-state"
            if necessaryScope not in self.scopes:
                self.addScope(necessaryScope)
                
            self.spotifyObject.pause_playback()

    def previousSong(self):
        if self.songPlaying():
            necessaryScope = "user-modify-playback-state"
            if necessaryScope not in self.scopes:
                self.addScope(necessaryScope)
                
            self.spotifyObject.previous_track()
    
    def getCurrentDevice(self):
        pass