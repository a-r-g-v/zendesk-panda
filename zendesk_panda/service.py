from typing import List

from slacker import Slacker
from zenpy import Zenpy

from zendesk_panda.usecase import Ticket


def sent_into_slack(slack_api_token: str, channel: str, message: str) -> None:
    Slacker(slack_api_token).chat.post_message(channel, message)


def get_unclosed_tickets(email: str, token: str, subdomain: str) -> List[Ticket]:
    return [Ticket()]