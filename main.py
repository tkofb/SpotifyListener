from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()

clientId = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")
tuiClientId =  os.getenv("TUI_CLIENT_ID")
tuiClientSecret = os.getenv("TUI_CLIENT_SECRET")

manualURL = "https://api.spotify.com/authorize?client_id=a56254b176ed4cf3b19c23b8c01c8507&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8888%2Fcallback"
scope = "&scope=user-read-currently-playing"

def requestUserAuthorization():
    url = "http://api.spotify.com/authorize"

    query = {
        "client_id": clientId,
        "response_type": "code",
        "redirect_uri": "http://localhost:8888/callback",
        "scope" : "user-read-currently-playing"
    }

    result = requests.get(url, params=query)
    
    print(result.request.url == url + scope)
    print(result.request.url)
    print(manualURL+scope)
    print(query)
    print(result.status_code)

requestUserAuthorization()
