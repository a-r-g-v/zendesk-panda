from typing import Iterable

from slacker import Slacker
from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket as ZendeskTicket, User as ZendeskUser

from zendesk_panda.usecase import Ticket


def sent_into_slack(slack_api_token: str, channel: str, message: str) -> None:
    Slacker(slack_api_token).chat.post_message(channel, message)


def get_unclosed_tickets(email: str, token: str, subdomain: str) -> Iterable[Ticket]:
    zenpy = Zenpy(subdomain, email, token)
    ticket: ZendeskTicket
    for ticket in zenpy.tickets():
        requester: ZendeskUser = ticket.requester
        waiting_on = None
        staled_at = None
        yield Ticket(ticket.id, ticket.subject, requester.email, requester.email, ticket.status, waiting_on, staled_at, ticket.created_at)
