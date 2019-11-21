from datetime import datetime, timedelta

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


