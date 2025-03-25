import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from unittest.mock import MagicMock

from app.utlis.spotify_token import generate_access_token 

def test_generate_access_token_success(mocker):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'access_token': 'valid-token'}
    
    mocker.patch("requests.post", return_value=mock_response)
    
    result = generate_access_token()
    
    assert result == 'valid-token'


def test_generate_access_token_error(mocker):
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.text = "Invalid request"
    
    mocker.patch("requests.post", return_value=mock_response)
    
    with pytest.raises(Exception, match="Error while generating the access token."):
        generate_access_token()


def test_missing_client_id_or_secret(mocker):
    mocker.patch("os.getenv", return_value=None)
    
    with pytest.raises(Exception, match="Error while generating the access token."):
        generate_access_token()


def test_missing_access_token_in_response(mocker):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}
    
    mocker.patch("requests.post", return_value=mock_response)
    
    with pytest.raises(Exception, match="Error while generating the access token."):
        generate_access_token()
