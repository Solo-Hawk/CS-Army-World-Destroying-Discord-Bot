import os, sys
import typing
import discord
import json

class StarboardPlugin:
    """Starboard plugin"""

    starboard_channel_id = ""
    configs = {"min_stars" :[1], "accepted_emojis":["star", "star2"] }

    async def setStarboard(message, discord_client: object) -> str:
        StarboardPlugin.starboard_channel_id = message.channel.id
        await discord_client.send_message(message.channel, "Starboard was set to this channel")

    async def on_reaction_add(reaction, user, discord_client: object):
        await discord_client.send_message(reaction.message.channel, reaction.emoji)
        if reaction.emoji in StarboardPlugin.configs["accepted_emojis"]:
            reactionCnt = 0
            # get all votes
            temp = reaction.message.reactions
            for r in temp:
                if r.emoji.name in StarboardPlugin.configs["accepted_emojis"]:
                    reactionCnt += r.count
            if reactionCnt >= StarboardPlugin.configs["min_stars"]:
                await StarboardPlugin.postToBoard(reaction.message)
                print(reaction.message)

    async def postToBoard(message, discord_client: object):
        if StarboardPlugin.starboard_channel_id != "" :
            await discord_client.send_message(client.get_channel(starboard_channel_id), message.content)
        



