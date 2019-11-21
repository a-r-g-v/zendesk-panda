import pytest

from zendesk_panda.config import load_config


def test_load_config():
    with pytest.raises(KeyError):
        load_config(source={})