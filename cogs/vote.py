import discord
from discord.ext import commands

class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send("pong!")

async def setup(bot):
    await bot.add_cog(Vote(bot))