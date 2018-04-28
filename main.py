#!/usr/bin/env python3

description = """
uh devon crawford bot lmao
"""

# import packages
import os
import sys
import configparser
import asyncio
import logging.config
from discord.ext import commands
import discord

print("loading bot using python version", sys.version)

# initialize logging? :thonk:
logging.config.fileConfig('resources/logging.cfg')

# read token
config = configparser.ConfigParser()
config.read("config.ini")

# sets working directory to bot's folder
# NOTE: Adding this so we can create .jsons in the future that contain timebans, muted members, etc.
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
print('Bot directory: ', dir_path)

prefix = ['!', '.']
bot = commands.Bot(command_prefix=prefix, description=description, pm_help=None)

# defines channels we may want to use
for server in bot.servers:
    bot.general = discord.utils.get(server.channels, name="general")
# end defining channels

# define addons
addons = [
    'addons.blah',
]

# create array for storing failed addons
failed_addons = []

# load the addons
for extension in addons:
    try:
        bot.load_extension(extension)
    except Exception as e: #uh-oh
        print('{} failed to load.\n{}: {}'.format(extension, type(e).__name__, e))
        failed_addons.append([extension, type(e).__name__, e])

# console
msg = "Bot has started!"
if len(failed_addons) != 0:
    msg += "\n\nSome addons failed to load:\n"
    for f in failed_addons:
        msg += "\n{}: `{}: {}`".format(*f)
print(msg)

# execute
bot.run(config['Main']['token'])
