import os, sys
import typing

class TestPlugin:
    def echo_func(discord_client: object) -> str:
        return "[TestPlugin] started __init__"

    def ping_func(discord_client: object) -> str:
        return "[TestPlugin] ping"
