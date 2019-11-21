from zendesk_panda.service import sent_into_slack


def test_sent_into_slack(config):
    sent_into_slack(config['slack_api_token'], config['slack_channel'], "test")