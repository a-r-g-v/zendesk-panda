import pytest

from zendesk_panda.config import load_config


def test_load_config_raises_key_error():
    with pytest.raises(KeyError):
        load_config(source={})


def test_load_config():
    source = dict(
        ZENDESK_EMAIL = "ZENDESK_EMAIL",
        ZENDESK_TOKEN = "ZENDESK_TOKEN",
        ZENDESK_SUBDOMAIN = "ZENDESK_SUBDOMAIN",
        SLACK_API_TOKEN = "SLACK_API_TOKEN",
        SLACK_CHANNEL = "SLACK_CHANNEL",

    )
    config = load_config(source)

    assert config["zendesk_email"] == "ZENDESK_EMAIL"
    assert config["zendesk_token"] == "ZENDESK_TOKEN"
    assert config["zendesk_subdomain"] == "ZENDESK_SUBDOMAIN"
    assert config["slack_api_token"] == "SLACK_API_TOKEN"
    assert config['slack_channel'] == "SLACK_CHANNEL"
