from typing import List

from zendesk_panda.model import Ticket


def generate_remind_message(tickets: List[Ticket]) -> str:
    header = "Waiting for response\n"
    message = ""

    for ticket in tickets:
        message += (f"[#{ticket.id}] {ticket.title} ({ticket.requester_slack}, {ticket.requester})\n" +
                    f"{ticket.staled} stale · {ticket.created} old · {ticket.status} · Waiting on {ticket.waiting_on}")

    return header + message + "\n"

