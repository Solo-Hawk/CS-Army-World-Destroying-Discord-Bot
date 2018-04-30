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
		config = {"RoleReactions":["emoji0", "emoji1", "emoji2", "emoji3"] "role0"= "rolenumber0", "role1"= "rolenumber1", "role2"= "rolenumber2", "role3"= "rolenumber3",}
	async def setSelfRole(message, discord_client: object) -> str:
		self.SelfRole_message_id = message.id
		await discord_client.send_message(message.channel, "SelfRoles was set to" + reactionmessageid + "message")

	async def setReaction (self,msg, rolenumber, roleid, reaction):
		"""Syntax:  !setReaction 'integer' 'roleid' 'reactionstring' """
		"""!setReaction 1 439568811822284801 :thanksjustin:"""
		try:
			self.rolenumber = message (13)
			self.rolenumber = int(rolenumber)
			self.SelfRole_ids  [rolenumber] = message (14:33)
			self.SelfRole_ids = int(SelfRole_ids [rolenumber])
			self.SelfRole_reaction [rolenumber] = message (35:end)
		except ValueError:
			await bot.say (message.channel,"Learn to use syntax, that's why i'll destroy world. (Syntax is !setReaction 'integer' 'roleid' 'reaction'")

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
