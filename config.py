#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7350085099:AAHQ6uYn3uFPpf0o4p_BrDrf9MM4Fz41iSU")
    API_ID = int(os.environ.get("API_ID", "23900056"))
    API_HASH = os.environ.get("API_HASH", "db7e21e638bc2359907814f4ed8b48a8")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7459282233")
