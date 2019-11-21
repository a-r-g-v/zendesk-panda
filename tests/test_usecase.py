from datetime import timedelta, datetime

from zendesk_panda.usecase import generate_remind_message
from zendesk_panda.model import Ticket


def test_generate_remind_message():
    datetime_2_days_ago = datetime.now() - timedelta(days=2)
    ticket = Ticket(1, "見積もり依頼", "argvc0@gmail.com", "a-r-g-v", "Open", "@agent1, @agent2, @agent3", datetime_2_days_ago, datetime_2_days_ago)

    expected = ( "Waiting for response\n" +
    "[#1] 見積もり依頼 (a-r-g-v, argvc0@gmail.com)\n" +
    "2 days stale · 2 days old · Open · Waiting on @agent1, @agent2, @agent3\n" )

    assert generate_remind_message([ticket]) == expected
