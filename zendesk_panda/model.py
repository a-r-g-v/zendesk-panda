from datetime import datetime, timedelta

from humanize import naturaldelta


class Ticket:
    def __init__(self, _id, title, requester, requester_slack, status, waiting_on, staled_at, created_at):
        self.id = _id
        self.title = title
        self.requester = requester
        self.requester_slack = requester_slack
        self.status = status
        self.waiting_on = waiting_on
        self.staled_at = staled_at
        self.created_at = created_at

    @property
    def staled(self) -> str:
        return naturaldelta(self.staled_at)

    @property
    def created(self) -> str:
        return naturaldelta(self.created_at)


