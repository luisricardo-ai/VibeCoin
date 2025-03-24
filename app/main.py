from dotenv import load_dotenv
from pathlib import Path
import os

import requests

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

def generate_access_token() -> str:
    """
    Function to generate the Spotify's access token

    Returns:
        str: The access token.
    """
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": str(os.getenv("SPOTIFY_CLIENT_ID")),
        "client_secret": str(os.getenv("SPOTIFY_CLIENT_SECRET"))
    }

    response = requests.post(url="https://accounts.spotify.com/api/token", headers=headers, data=data)

    if response.status_code != 200:
        raise Exception("Error while generating the access token.")
    
    access_token = response.json().get('access_token')
    if not access_token:
        raise Exception("Error while generating the access token: access_token missing.")
    
    return access_token

if __name__ == "__main__":
    access_token = generate_access_token()
    print("Access token generated!")