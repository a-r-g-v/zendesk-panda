from slacker import Slacker


def sent_into_slack(slack_api_token, channel, message):
    Slacker(slack_api_token).chat.post_message(channel, message)
