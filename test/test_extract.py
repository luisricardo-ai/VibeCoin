import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from unittest.mock import patch, mock_open
from app.ETL.extract import check_input_folder, playlist  # Replace 'your_module' with the actual module name

def test_check_input_folder(tmp_path):
    folder = tmp_path / "data/input"
    check_input_folder(str(folder))
    assert folder.is_dir()

@patch("requests.get")
@patch("builtins.open", new_callable=mock_open)
@patch("os.makedirs")
@patch("os.path.isdir", return_value=False)  # Mock to ensure makedirs is called
def test_playlist(mock_isdir, mock_makedirs, mock_open_file, mock_requests):
    playlist_id = "test_playlist_id"
    access_token = "test_access_token"
    folder = "././data/input"

    mock_response = mock_requests.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"name": "Test Playlist", "tracks": []}

    playlist(playlist_id, access_token)

    mock_requests.assert_called_once_with(
        f"https://api.spotify.com/v1/playlists/{playlist_id}",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    mock_open_file.assert_called_once_with(f"{folder}/spotify_playlist.json", "w", encoding="utf-8")
    mock_makedirs.assert_called_once_with(folder)


def test_playlist_api_error(mocker):
    mock_requests = mocker.patch("requests.get")
    mock_requests.return_value.status_code = 404
    mock_requests.return_value.content = b"Not Found"
    
    with pytest.raises(Exception, match="Error 404 while requesting 'get' from API. b'Not Found'"):
        playlist("invalid_id", "test_access_token")
