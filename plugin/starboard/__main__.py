import os, sys
import typing
import discord
import json

class StarboardPlugin:
    """Starboard plugin"""

    starboard_channel_id = ""
    configs = {"min_stars" :[10], "accepted_emojis":[] }

    async def loadConfigs(discord_client: object):
        manifest = json.load("manifest.json","r")

        for i in manifest["configs"]:
            self.configs["min_stars"] = i["min_stars"]
            self.configs["accepted_emojis"] = i["accepted_emojis"]

    async def setStarboard(message, discord_client: object) -> str:
        starboard_channel_id = message.channel

    async def on_reaction_add(reaction, user, discord_client: object):
        if reaction.emoji.name in configs["accepted_emojis"]:
            reactionCnt = 0
            # get all votes
            temp = reaction.message.reactions
            for r in temp:
                if r.emoji.name in configs["accepted_emojis"]:
                    reactionCnt += r.count
            if reactionCnt >= configs["min_stars"]:
                await postToBoard(reaction.message)

    async def postToBoard(message, discord_client: object):
        if starboard_channel_id != "" :
            await discord_client.send_message(client.get_channel(starboard_channel_id), message.content)
        



