import logging
import discord
import datetime
import os
import json
import importlib.util

logger = logging.getLogger(__name__)

discord_client = discord.Client()

main_channel_id = '402577355559796747'

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
       self.plugin_exports = []
       self.callback = {"on_message" : []}
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
            self.plugin_exports.append({"plugin": f"{temp['plugin']}", "class": getattr(plugin, temp['plugin'])})

            for callable_function in temp["accepts"]:
                self.callback[callable_function['on_event']].append({
                    "command": callable_function['command'],
                    "callback": callable_function['callback']})

            loaded_plugins.append(f"{temp['plugin']}@{temp['plugin_ver']}")
        return loaded_plugins

    def find_callback(self, __type: str, prefix: str) -> str:
        temp = self.callback[__type]
        for command in temp:
            if command['command'] == prefix:
                return command['callback']
            else:
                pass
        return "ERROR 5112"

    def parse_callback(self, callback: str) -> object:
        temp = callback.split('@')
        print(self.plugin_exports)
        for i in self.plugin_exports:
            if i['plugin'] == temp[-1]:
                return getattr(i['class'], temp[0])
        return "5512"


discord_bot = DiscordBot()

@discord_client.event
async def on_ready():
    await discord_client.send_message(discord.Object(id=main_channel_id), f" Bot init ")
    logger.debug(discord_client.user.name)
    logger.debug(discord_client.user.id)
    logger.debug('------')
    for i in discord_bot._parse_plugin_manifests():
        await discord_client.send_message(discord.Object(id=main_channel_id), f"{i} ... OK")


@discord_client.event
async def on_message(message):
    __type__ = "on_message"

    callback = discord_bot.find_callback(__type__, message.content.split(' ')[0])
    if callback != "5112":
        to_call = discord_bot.parse_callback(callback)
        if to_call != "5512":
            await to_call(message.channel, discord_client)

