#!/usr/bin/env python
# -*- coding:utf-8 -*-

import slackweb

def slack_post(posting_url, posting_channel, posting_text):
    slack = slackweb.Slack(url = str(posting_url))
 
    slack.notify(
        text= unicode(posting_text), 
        channel= str(posting_channel),
        mrkdwn=True
    )




