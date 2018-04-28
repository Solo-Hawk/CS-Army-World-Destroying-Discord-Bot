import logging
import discord
import datetime
import os
import json
import importlib.util

logger = logging.getLogger(__name__)

discord_client = discord.Client()

def get_token(file):

    with open(file, 'r') as f:
        password = f.read()

    return str(password)


class DiscordBot():
    def __init__(self):
       self.path = os.path.dirname(os.path.realpath("./"))
       self.plugins = []
       self.plugin_manifest = json.load(open(f"{self.path}/plugin/manifest.json", "r"))
       self.manifests = []
       self.plugin_exports = {}
       self._load_plugin_manifest()

    def _load_plugin_manifest(self):
        for i in self.plugin_manifest["plugins"]:
            self.manifests.append(f"{self.path}/plugin/{i}")

    def _parse_plugin_manifests(self):
        loaded_plugins = []
        for i in self.manifests:
            temp = json.load(open(f"{i}"))
            self.plugins.append(temp)
            spec = importlib.util.spec_from_file_location(temp['plugin'], f"{os.path.split(i)[0]}/{temp['plugin_object']}")
            plugin = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(plugin)
            self.plugins.append({"plugin": f"{temp['plugin']}", "class": getattr(plugin, temp['plugin'])})
            loaded_plugins.append(f"{temp['plugin']}@{temp['plugin_ver']}")
        return loaded_plugins

discord_bot = DiscordBot()

@discord_client.event
async def on_ready(self):
    logger.debug(discord_client.user.name)
    logger.debug(discord_client.user.id)
    logger.debug('------')
    for i in discord_bot._parse_plugin_manifests():
        await discord.client.send_message(discord.Object(id='439598709299347456'), f"{i} ... OK")


@discord_client.event
async def on_message(self, message):
    if message.content.startswith(prefix + 'ping'):
        to_send = f"{str(message.timestamp - datetime.datetime.utcnow())} s"
        await discord_client.send_message(message.channel, "Pong - Response time {to_send}")
        print(message.timestamp - datetime.datetime.utcnow())
