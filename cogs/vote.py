import discord
from discord.ext import commands

class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='vote')
    async def vote(self, ctx, *args):
        question = ' '.join(args[:-1])
        answers = options[-1]

        embed = discord.Embed(title = question, description=answers)

        message = await ctx.send(embed = embed)

        for arg in range(len(options)-1):
            await message.add_reaction(chr(127462 + i))

async def setup(bot):
    await bot.add_cog(Vote(bot))