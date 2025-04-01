import json
import os
import pandas as pd

def check_output_folder(folder: str):
    """
    Function to check and create `data/output` folder.

    Args:
        folder (str): Folder path.
    """
    if os.path.isdir(folder) == False:
        os.makedirs(folder)

def read_json(path: str) -> dict:
    """
    Function to read json data.

    Args:
        path (str): The file's path.

    Return:
        dict: File content.
    """

    if os.path.exists(path) == False:
        raise Exception(f"Error: {path} does not exists.")

    with open(path, 'r', encoding='utf-8') as file:
        content = json.load(file)

    return content

def filter_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Function to filter desired columns.

    Args:
        data (pd.DataFrame): The dataframe to remove columns

    Returns:
        pd.DataFrame: The new dataframe.
    """
    desired_columns = ['added_at', 'added_by.id', 'added_by.type', 'track.available_markets', 'track.album.id', 'track.artists', 'track.id', 'track.name', 'track.popularity', 'ranking']
    return data.filter(items=desired_columns)

def playlist(path: str):
    """
    Function to transform the playlist data.

    Args:
        path (str): Path to the file
    """
    folder = "././data/output"
    check_output_folder(folder=folder)

    content = read_json(path)

    df = pd.json_normalize(content["results"]["tracks"]["items"])
    df = filter_columns(data=df)
    df["ranking"] = df.index + 1
    
    df.to_csv(f"{folder}/spotify_playlist.csv")