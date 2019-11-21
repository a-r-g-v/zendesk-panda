
def generate_remind_message() -> str:
    header = "Waiting for response\n"

    ticket = ("[#1] 見積もり依頼 (a-r-g-v, argvc0@gmail.com)\n" +
    "2 days stale · 2 days old · Open · Waiting on @agent1, @agent2, @agent3")


    return header + ticket + "\n"
