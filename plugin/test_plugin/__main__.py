import os, sys
import typing

class TestPlugin:
    def ping_func(discord_client: object) -> str:
        return "[TestPlugin] started __init__"

    async def echo_func( message_channel, discord_client: object) -> str:
        await discord_client.send_message(message_channel, "echo func works fine")
