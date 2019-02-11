#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import subprocess

from slackbot.bot import Bot
from slackbot.bot import respond_to

@respond_to(r'.*')
def mention_func(message):
    message.reply(subprocess.check_output("ip addr", shell=True))

def main():
    bot = Bot()
    bot.run()

def daemonize():
    pid = os.fork()
    if pid > 0:
        print("If you exec as not service, a permission error occurs. Please ignore and kill a child process.")
        print("Parent process pid: {}".format(pid))
        pid_file = open("/var/run/notice-ip-to-slack.pid", "w")
        pid_file.write(str(pid) + "\n")
        pid_file.close()
        sys.exit()
    if pid == 0:
        print("Child process pid: {}".format(pid))
        main()

if __name__ == "__main__":
    daemonize()
