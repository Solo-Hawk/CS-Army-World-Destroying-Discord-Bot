import os, sys
import typing
import discord

class TestPlugin:
    async def ping_func(message, discord_client: object) -> str:
        await discord_client.send_message(message.channel, "WE WUZ KINGS N SHIET")

    async def echo_func( message, discord_client: object) -> str:
        await discord_client.send_message(message.channel, message.content.split("!echo ")[-1])

    async def echoto_func(message, discord_client: object) -> str:
        temp = message.content.split()
        await discord_client.send_message(discord.Object(id=temp[1]), temp[2])
