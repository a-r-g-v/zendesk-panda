import pytest

from zendesk_panda.config import load_config


@pytest.fixture
def config():
    try:
        return load_config()
    except KeyError:
        pytest.skip("failed to load config from environment variables")