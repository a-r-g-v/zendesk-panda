from zendesk_panda.usecase import generate_remind_message


def test_generate_remind_message():
    expected = """Waiting for response
    [#1] 見積もり依頼 (a-r-g-v, argvc0@gmail.com)
    2 days stale · 2 days old · Waiting on @agent1, @agent2, @agent3
    """

    assert generate_remind_message() == expected