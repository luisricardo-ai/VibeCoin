import pandas as pd
import requests
import urllib.parse

def main(df: pd.DataFrame, access_token:str):
    """
    Function to get song details
    """

    header = {
        "Authorization": f"Bearer {access_token}"
    }

    df['query'] = df.apply(lambda row: f"track:{row['title']} artist:{row['artist']}", axis=1)
    df['encoded_query'] = df['query'].apply(urllib.parse.quote)
    
    for row in df['encoded_query']:
        content = requests.get(
            headers=header,
            url=f"https://api.spotify.com/v1/search?type=track&query={row}",
        )

        print(content.text)