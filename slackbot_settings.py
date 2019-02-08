# -*- coding: utf-8 -*-
import os
import subprocess

API_TOKEN = os.getenv("BOT_SLACK_TOKEN")

default_reply = subprocess.check_output("ip addr", shell=True)
