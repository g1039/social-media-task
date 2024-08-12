from unittest.mock import patch, MagicMock

from utility import SocialMediaUtil

@patch('requests.get')
def test_social_media_count_valid_response(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = [{"facebook": 1}, {"instagram": 2}, {"twitter": 3}]
    mock_get.return_value = mock_response

    util = SocialMediaUtil()

    util.social_media_count("https://takehome.io/twitter", "twitter")
    assert util.results['twitter'] == 3


@patch('requests.get')
def test_social_media_count_invalid_response(mock_get):
    mock_response = MagicMock()
    mock_response.json.side_effect = ValueError("Invalid JSON")
    mock_get.return_value = mock_response

    util = SocialMediaUtil()

    util.social_media_count("https://takehome.io/twitter", "twitter")

    assert util.results['twitter'] == 0


@patch.object(SocialMediaUtil, 'social_media_count')
def test_social_media_thread(mock_social_media_count):
    util = SocialMediaUtil()

    mock_social_media_count.side_effect = lambda url, platform: util.results.update({platform: len(platform)})

    result = util.social_media_thread()

    assert result == {
        "twitter": len("twitter"),
        "facebook": len("facebook"),
        "instagram": len("instagram")
    }
