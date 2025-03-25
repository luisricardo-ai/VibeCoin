import requests
import json
import os

def check_input_folder(folder: str):
    """
    Function to check and create `data/input` folder.

    Args:
        folder (str): Folder path.
    """
    if os.path.isdir(folder) == False:
        os.makedirs(folder)

def playlist(playlist_id: str, access_token: str):
    """
    Function to extract the playlist data.

    Args:
        playlist_id (str): Spotify playlist identifier.
        access_token (str): The access token for Spotify API.
    """
    folder = "././data/input"
    check_input_folder(folder=folder)

    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open(f"{folder}/spotify_playlist.json", "w", encoding="utf-8") as json_file:
            json.dump(response.json(), json_file, indent=4)

    else:
        raise Exception(f"Error {response.status_code} while requesting 'get' from API. {response.content}")