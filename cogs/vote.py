import discord
from discord.ext import commands

class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='vote')
    async def vote(self, ctx, *options):
        question = options[0]
        answers = ' '.join(options[1:])

        embed = discord.Embed(title = question, description=answers, color = discord.Color.green())

        message = await ctx.send(embed = embed)

        for i in range(len(options)-1):
            await message.add_reaction(chr(127462 + i))

        reactions = await message.await_reactions(timeout=1)

        result = []

        for i, reaction in enumerate(reactions):
            result.append(f'{options[i]}: {reaction.count -1}표')
        await ctx.send('\n'.join(result))

async def setup(bot):
    await bot.add_cog(Vote(bot))