import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.ETL.transform import read_json, playlist, filter_columns, check_output_folder

import json
import pytest
import pandas as pd
from unittest.mock import patch, mock_open

# Testes para check_output_folder
@patch("os.path.isdir", return_value=True)
@patch("os.makedirs")
def test_check_output_folder_exists(mock_makedirs, mock_isdir):
    check_output_folder("data/output")
    mock_makedirs.assert_not_called()

@patch("os.path.isdir", return_value=False)
@patch("os.makedirs")
def test_check_output_folder_not_exists(mock_makedirs, mock_isdir):
    check_output_folder("data/output")
    mock_makedirs.assert_called_once_with("data/output")

# Testes para read_json
@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"key": "value"}))
def test_read_json(mock_file, mock_exists):
    result = read_json("file.json")
    assert result == {"key": "value"}

@patch("os.path.exists", return_value=False)
def test_read_json_file_not_found(mock_exists):
    with pytest.raises(Exception, match="Error: file.json does not exists."):
        read_json("file.json")

# Testes para filter_columns
def test_filter_columns():
    data = pd.DataFrame({
        'added_at': ['2024-03-01', '2024-03-02'],
        'added_by.id': ['user1', 'user2'],
        'added_by.type': ['admin', 'editor'],
        'track.available_markets': [['US', 'BR'], ['DE', 'FR']],
        'track.album.id': ['album1', 'album2'],
        'track.artists': [['artist1'], ['artist2']],
        'track.id': ['track1', 'track2'],
        'track.name': ['Song A', 'Song B'],
        'track.popularity': [80, 75],
        'ranking': [1, 2],
        'extra_column': ['ignore1', 'ignore2']
    })

    expected_data = pd.DataFrame({
        'added_at': ['2024-03-01', '2024-03-02'],
        'added_by.id': ['user1', 'user2'],
        'added_by.type': ['admin', 'editor'],
        'track.available_markets': [['US', 'BR'], ['DE', 'FR']],
        'track.album.id': ['album1', 'album2'],
        'track.artists': [['artist1'], ['artist2']],
        'track.id': ['track1', 'track2'],
        'track.name': ['Song A', 'Song B'],
        'track.popularity': [80, 75],
        'ranking': [1, 2]
    })

    result = filter_columns(data)
    pd.testing.assert_frame_equal(result, expected_data)

@patch("app.ETL.transform.check_output_folder")
@patch("app.ETL.transform.read_json", return_value={
    "results": {
        "tracks": {
            "items": [
                {"track": {"id": "1", "name": "Song A", "popularity": 90}},
                {"track": {"id": "2", "name": "Song B", "popularity": 80}}
            ]
        }
    }
})
@patch("app.ETL.transform.filter_columns", side_effect=lambda data: data)
@patch.object(pd.DataFrame, "to_csv")
def test_playlist(mock_to_csv, mock_filter, mock_read_json, mock_check_folder):
    input_path = "input.json"
    playlist(input_path)
    mock_check_folder.assert_called_once_with(folder="././data/output")
    mock_read_json.assert_called_once_with(input_path)
    mock_filter.assert_called_once()
    mock_to_csv.assert_called_once_with("././data/output/spotify_playlist.csv")