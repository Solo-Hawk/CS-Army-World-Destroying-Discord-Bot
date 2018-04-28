#!/usr/bin/env python3

import logging.config
from discordClient import discord_client, get_token
#from config.config import token
import sys

# Initialize Logging
logging.config.fileConfig('../config/logging.cfg')


def main():

    discord_client.run(sys.argv[1])


if __name__ == '__main__':
    main()
