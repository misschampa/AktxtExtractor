#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "29882686"))
    API_HASH = os.environ.get("API_HASH", "b642a25aee67b2aed02116df4a916bca")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7459282233")
