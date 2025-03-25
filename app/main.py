from dotenv import load_dotenv
from pathlib import Path

# Token
from utlis.spotify_token import generate_access_token

# ETL imports
import ETL.extract

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

if __name__ == "__main__":
    playlist_id = "5FN6Ego7eLX6zHuCMovIR2"
    access_token = generate_access_token()
    print("Access token generated!")

    ETL.extract.playlist(
        playlist_id=playlist_id,
        access_token=access_token
    )