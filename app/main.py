from dotenv import load_dotenv
from pathlib import Path
import pandas as pd

# Token
from utlis.spotify import token
from ETL.spotify_extract import extract

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

if __name__ == "__main__":
    df = pd.read_csv("./charts.csv")
    df = df[
        (df['region'] == 'Global')
        & (df['rank'] == 1)
    ]

    spotify_token = token()

    extract(df, access_token=spotify_token)
