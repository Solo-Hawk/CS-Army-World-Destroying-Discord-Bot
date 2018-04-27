import logging.config
from resources.discordClient import discord_client, get_token


# Initialize Logging
logging.config.fileConfig('resources/logging.cfg')


def main():

    discord_client.run(get_token("resources/token.txt"))


if __name__ == '__main__':
    main()
