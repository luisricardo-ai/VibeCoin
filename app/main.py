from dotenv import load_dotenv
from pathlib import Path
import pandas as pd

# Token
from utlis.spotify_token import generate_access_token
from ETL.spotify_extract import main

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

if __name__ == "__main__":
    df = pd.read_csv("./charts.csv", nrows=10000)
    df = df[
        (df['region'] == 'Global') 
        & (df['date'] == '2017-01-01') # REMOVE
        & (df['rank'] == 1) # REMOVE
    ]

    access_token = generate_access_token()

    main(df, access_token)