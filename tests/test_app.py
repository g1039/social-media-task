import json
import pytest
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@patch('app.SocialMediaUtil')
def test_social_network_activity(mock_social_media_util, client):
    mock_social_media_util.return_value.social_media_thread.return_value = {
        "facebook": 2,
        "twitter": 5,
        "instagram": 1
    }

    response = client.get('/')
    assert response.status_code == 200
    
    data = json.loads(response.data)

    assert isinstance(data, dict)
    
    assert data == {
        "facebook": 2,
        "twitter": 5,
        "instagram": 1
    }

    mock_social_media_util.return_value.social_media_thread.assert_called_once()
