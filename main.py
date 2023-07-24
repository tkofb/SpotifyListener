from dotenv import load_dotenv
import os
import base64
import json
from requests import post, get

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def getToken():
    authorizationString = client_id + ":" + client_secret
    authorizationBytes = authorizationString.encode("utf-8")
    authorizationBase64 = str(base64.b64encode(authorizationBytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + authorizationBase64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    result = post(url, headers=headers, data=data)
    jsonResult = json.loads(result.content)
    token = jsonResult["access_token"]
    return token

def getAuthorizationHeader(token):
    return {"Authorization": "Bearer " + token}

def searchForArtist(token, artistName):
    url = "https://api.spotify.com/v1/search"
    headers = getAuthorizationHeader(token)
    query = f"?q={artistName}&type=artist&limit=1"

    queryURL = url + query
    result = get(queryURL, headers=headers)
    jsonResult = json.loads(result.content)["artists"]["items"]
    if len(jsonResult) == 0:
        print("No Sauze")
        return None
    return jsonResult[0]

def getSongsByArtist(token,artistID):
    url = "https://api.spotify.com/v1/artists/{}/top-tracks?country=US".format(artistID)
    headers = getAuthorizationHeader(token)
    result = get(url, headers = headers)
    jsonResult = json.loads(result.content)["tracks"]
    return jsonResult

token = getToken()
artist = searchForArtist(token, "Frank Ocean")
artistID = artist["id"]
print(artistID)
songs = getSongsByArtist(token, artistID)

for i, song in enumerate(songs):
    print("{}. {}".format(i+1,song['name']))
