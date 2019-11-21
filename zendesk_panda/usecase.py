from typing import List

class Ticket:
    def __init__(self):
        self.id = 1
        self.title = "見積もり依頼"
        self.requester_slack = "a-r-g-v"
        self.requester = "argvc0@gmail.com"
        self.status = "Open"
        self.staled = "2 days"
        self.created = "2 days"
        self.waiting_on = "@agent1, @agent2, @agent3"


def generate_remind_message(tickets: List[Ticket] = [Ticket()]) -> str:
    header = "Waiting for response\n"
    message = ""

    for t in tickets:
        message += ("[#{id}] {title} ({requester_slack}, {requester})\n".format(**t.__dict__) +
        "{staled} stale · {created} old · {status} · Waiting on {waiting_on}".format(**t.__dict__))


    return header + message + "\n"
