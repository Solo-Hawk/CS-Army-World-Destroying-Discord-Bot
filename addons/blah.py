import discord
from discord.ext import commands
from sys import argv

class Things:
    """
    Random things.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.command()
    async def ping(self):
        """About the bot"""
        await self.bot.say("pong!")



def setup(bot):
    bot.add_cog(Things(bot))
