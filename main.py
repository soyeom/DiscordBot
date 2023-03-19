import discord, os, asyncio
from discord.ext import commands

async def main():
    prefix = '/'
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix=prefix, intents=intents)

    await bot.load_extension('cogs.vote')

    with open('token.txt', 'r') as f:
        token = f.read()

    await bot.start(token)

if __name__ == '__main__':
    asyncio.run(main())