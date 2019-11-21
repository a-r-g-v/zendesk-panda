from datetime import datetime, timedelta

from humanize import naturaldelta


class Ticket:
    def __init__(self):
        pass

    @property
    def staled(self) -> str:
        return naturaldelta(self.staled_at)

    @property
    def created(self) -> str:
        return naturaldelta(self.created_at)


