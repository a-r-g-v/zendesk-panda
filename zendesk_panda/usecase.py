from datetime import datetime, timedelta
from typing import List

class Ticket:
    def __init__(self):
        self.id = 1
        self.title = "見積もり依頼"
        self.requester_slack = "a-r-g-v"
        self.requester = "argvc0@gmail.com"
        self.status = "Open"
        self.waiting_on = "@agent1, @agent2, @agent3"
        self.created_at = datetime.now() - timedelta(days=2)
        self.staled_at = datetime.now() - timedelta(days=2)

    @property
    def staled(self):
        return str((datetime.now() - self.staled_at).days) + " days"

    @property
    def created(self):
        return str((datetime.now() - self.created_at).days) + " days"


def generate_remind_message(tickets: List[Ticket]) -> str:
    header = "Waiting for response\n"
    message = ""

    for ticket in tickets:
        message += (f"[#{ticket.id}] {ticket.title} ({ticket.requester_slack}, {ticket.requester})\n" +
                    f"{ticket.staled} stale · {ticket.created} old · {ticket.status} · Waiting on {ticket.waiting_on}")

    return header + message + "\n"

