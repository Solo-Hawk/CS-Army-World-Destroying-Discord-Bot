import os, sys
import typing

class TestPlugin:
    async def ping_func(message, discord_client: object) -> str:
        await discord_client.send_message(message.channel, "WE WUZ KINGS N SHIET")

    async def echo_func( message, discord_client: object) -> str:
        await discord_client.send_message(message.channel, message.content.split("!echo ")[-1])
