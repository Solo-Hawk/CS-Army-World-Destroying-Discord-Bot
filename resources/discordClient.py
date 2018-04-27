import logging
import discord
import datetime

prefix = "!"
logger = logging.getLogger(__name__)



discord_client = discord.Client()


def get_token(file):

    with open(file, 'r') as f:
        password = f.read()

    return str(password)


@discord_client.event
async def on_ready():
    logger.debug(discord_client.user.name)
    logger.debug(discord_client.user.id)
    logger.debug('------')


@discord_client.event
async def on_message(message):

    if message.content.startswith(prefix + 'ping'):

        await discord_client.send_message(message.channel, "Pong - Response time " + str(message.timestamp - datetime.datetime.utcnow()) + " s")
    print(message.timestamp - datetime.datetime.utcnow())
