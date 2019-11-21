from typing import List

from zendesk_panda.service import sent_into_slack
from zendesk_panda.usecase import Ticket


def test_sent_into_slack(config):
    sent_into_slack(config['slack_api_token'], config['slack_channel'], "test")


def test_get_unclosed_tickets(config):
    tickets: List[Ticket] = get_unclosed_tickets(config['zendesk_email'], config['zendesk_token'], config['zendesk_subdomain'])
    assert len(tickets) == 1
    assert tickets[0].id == 1