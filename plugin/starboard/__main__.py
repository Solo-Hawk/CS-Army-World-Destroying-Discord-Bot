import os, sys
import typing
import discord
import json

class StarboardPlugin(object):
    """Starboard plugin"""

    def __init__(self):
        self.starboard_channel_id = None
        self.min_stars = 1
        self.accepted_emoji = '⭐'
        self.posted_message_id = []

    async def setStarboard(message, discord_client: object) -> str:
        self.starboard_channel_id = message.channel.id
        await discord_client.send_message(message.channel, "Starboard was set to this channel")

    async def on_reaction_add(reaction, user, discord_client: object):
        if reaction.message.id in posted_message_id:
            return;
        
        if reaction.emoji == self.accepted_emoji:
            if reaction.count >= self.min_stars:
                await self.postToBoard(reaction.message)
                posted_message_id.append(reaction.message.id)

    async def postToBoard(message, discord_client: object):
        if self.starboard_channel_id != None :
            await discord_client.send_message(client.get_channel(self.starboard_channel_id), message.content)
        



