import os, sys
import typing
import discord
import json

class RolesPlugin(object):
    """Roles plugin"""
	def __init__ (self):
		SelfRole_message_id = None
		SelfRole_ids = []
		SelfRole_reactions = []
	async def on_reaction_add(reaction, user):
		if reaction.message == self.SelfRole_message_id:
			for x in xrange(len(self.SelfRole_reactions)):
				if reaction == self.SelfRole_rections[x]:
					try:
						await bot.add_roles(user,self.SelfRole_ids[x])
					except discord.errors.Forbidden:
						await bot.say(reaction.message.channel, "There was an error giving {0.RolesPlugin.SelfRole_ids[x]} to {0.user}!")
			else:
				try:
					await remove_reaction(message=reaction.message, emoji=reaction, member=user)
				except InvalidArgument:
					await bot.say(reaction.message.channel, "Something wrong with removing nonexisting emotes.")
