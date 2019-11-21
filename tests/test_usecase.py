from zendesk_panda.usecase import generate_remind_message
from zendesk_panda.model import Ticket


def test_generate_remind_message():
    expected = ( "Waiting for response\n" +
    "[#1] 見積もり依頼 (a-r-g-v, argvc0@gmail.com)\n" +
    "2 days stale · 2 days old · Open · Waiting on @agent1, @agent2, @agent3\n" )

    assert generate_remind_message([Ticket()]) == expected
