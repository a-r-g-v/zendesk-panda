from datetime import datetime, timedelta
from typing import List

from humanize import naturaldelta


class Ticket:
    def __init__(self):
        self.id: int = 1
        self.title: str = "見積もり依頼"
        self.requester_slack: str = "a-r-g-v"
        self.requester: str = "argvc0@gmail.com"
        self.status: str = "Open"
        self.waiting_on: str = "@agent1, @agent2, @agent3"
        self.created_at: datetime = datetime.now() - timedelta(days=2)
        self.staled_at: datetime = datetime.now() - timedelta(days=2)

    @property
    def staled(self) -> str:
        return naturaldelta(self.staled_at)

    @property
    def created(self) -> str:
        return naturaldelta(self.created_at)


def generate_remind_message(tickets: List[Ticket]) -> str:
    header = "Waiting for response\n"
    message = ""

    for ticket in tickets:
        message += (f"[#{ticket.id}] {ticket.title} ({ticket.requester_slack}, {ticket.requester})\n" +
                    f"{ticket.staled} stale · {ticket.created} old · {ticket.status} · Waiting on {ticket.waiting_on}")

    return header + message + "\n"

