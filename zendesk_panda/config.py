import os
from typing import Dict

Config = Dict[str, str]


def load_config(source=os.environ) -> Config:
    """
    :raise: KeyError
    :rtype: Config
    """
    return {
        "email": source["ZENDESK_EMAIL"],
        "token": source['ZENDESK_TOKEN'],
        "subdomain": source["ZENDESK_SUBDOMAIN"],
    }