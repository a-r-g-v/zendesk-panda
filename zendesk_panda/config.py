import os
from typing import Dict

Config = Dict[str, str]


def load_config(source=os.environ) -> Config:
    """
    :raise: KeyError
    :rtype: Config
    """
    return {
        "zendesk_email": source["ZENDESK_EMAIL"],
        "zendesk_token": source['ZENDESK_TOKEN'],
        "zendesk_subdomain": source["ZENDESK_SUBDOMAIN"],
        "slack_api_token": source["SLACK_API_TOKEN"],
        "slack_channel": source["SLACK_CHANNEL"],
    }