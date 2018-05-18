import os, sys
import typing
import itertools

async def function_name(self, discord_plugin_manager, message, discord_client: object) -> None:

class AdminPlugin(object)
	async def plugins(discord_plugin_manager, message, discord_client: object) -> str:
		temp = []
		for i in discord_plugin_manager.plugin_exports:
			temp.append({"plugin": i['plugin'], "status": "active"})

		await discord_client.send_message(message.channel, "PLUGIN    STATUS")
		for i in temp:
			await discord_client.send_message(message.channel, f"{i['plugin']}  {i['status']}")

	def __init__ (self):
		modlog_channel_id = None
		mod_role_id = None

	async def kick(self, discord_plugin_manager, messages, user:discord.Member, reason:str=None, discord_client: object) -> None:
		"""Kicks someone from the server"""
		if reason is None:
			reason = "ask " + message.author + "why?"
		try:
			await bot.kick(user)
		except discord.errors.Forbidden:
			await bot.say("You deal with him. What am I an unconcious bot?")
			return

	async def ban(self, discord_plugin_manager, message, user:discord.Member, reason:str=None, discord_client: object) -> None:
		"""Bans the specified user from the server"""
		mod_role_name = read_data_entry(ctx.message.server.id, "Bot Mod")
		mod = discord.utils.get(ctx.message.author.roles, name=mod_role_name)
		if not mod:
			await self.bot.say("You have to git gud before doing that!")
			return
		if reason is None:
			reason = "ask " + message.author + "why?"
		try:
			await self.bot.ban(user, delete_message_days=0)
		except discord.errors.Forbidden:
			await self.bot.say("What you want me to conquer whole server? You know I can do that, but I'm lazy.")
			return
		await self.bot.say("Yeah, ban 'em, you all gonna be banned and server will be **MINE**")

	async def unban(self, discord_plugin_manager, message, username:str, discord_client: object) -> None:
		"""Unbans the user with the specifed name from the server"""
		mod_role_name = read_data_entry(self.message.server.id, "Bot Mod")
		mod = discord.utils.get(self.message.author.roles, name=mod_role_name)
		if not mod:
			await self.bot.say("How many more times do I have to say *git gud*.")
			return
		try:
			banlist = await self.bot.get_bans(self.message.server)
			user = discord.utils.get(banlist, name=username)
		if user is None:
			await self.bot.say("LOL. What a genius, who can't remember who to unban!"
			return
		await self.bot.unban(self.message.server, user)
		await self.bot.say("I'm not sure he deserves that but here, ya go. Unbanned.")
					   
