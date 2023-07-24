from dotenv import load_dotenv
import os
import base64
import json
from requests import post

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

token = getToken()
print(token)
