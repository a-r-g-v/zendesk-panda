from slacker import Slacker


def sent_into_slack(slack_api_token: str, channel: str, message: str) -> None:
    Slacker(slack_api_token).chat.post_message(channel, message)
