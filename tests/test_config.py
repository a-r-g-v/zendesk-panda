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

    )
    config = load_config(source)

    assert config["email"] == "ZENDESK_EMAIL"
    assert config["token"] == "ZENDESK_TOKEN"
    assert config["subdomain"] == "ZENDESK_SUBDOMAIN"