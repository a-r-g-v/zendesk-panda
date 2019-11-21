from datetime import timedelta, datetime

from zendesk_panda.usecase import generate_remind_message
from zendesk_panda.model import Ticket


def test_generate_remind_message():
    ticket = Ticket()
    ticket.id: int = 1
    ticket.title: str = "見積もり依頼"
    ticket.requester_slack: str = "a-r-g-v"
    ticket.requester: str = "argvc0@gmail.com"
    ticket.status: str = "Open"
    ticket.waiting_on: str = "@agent1, @agent2, @agent3"
    ticket.created_at: datetime = datetime.now() - timedelta(days=2)
    ticket.staled_at: datetime = datetime.now() - timedelta(days=2)

    expected = ( "Waiting for response\n" +
    "[#1] 見積もり依頼 (a-r-g-v, argvc0@gmail.com)\n" +
    "2 days stale · 2 days old · Open · Waiting on @agent1, @agent2, @agent3\n" )

    assert generate_remind_message([ticket]) == expected
