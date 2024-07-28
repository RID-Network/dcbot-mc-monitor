"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.2.0
"""

from discord.ext import commands
from discord.ext.commands import Context
import discord
from mcstatus import JavaServer
import os
MC_SERVER = os.getenv("MC_SERVER", 'localhost:25565')
server = JavaServer.lookup(MC_SERVER)
# Here we name the cog and create a new class for the cog.
class Minecraft(commands.Cog, name="minecraft"):
    def __init__(self, bot) -> None:
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="status",
        description="List players on the server.",
    )
    async def status(self, context: Context) -> None:
        print(MC_SERVER)
        status = server.status()
        embed = discord.Embed(
            description=f"The server has {status.players.online} player(s) online and replied in {status.latency} ms",
            color=0xE02B2B,
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="list",
        description="List players on the server.",
    )
    async def list_players(self, context: Context) -> None:
        print(MC_SERVER)
        query = server.query()
        embed = discord.Embed(
            description=f"The server has the following players online: {', '.join(query.players.names)}",
            color=0xE02B2B,
        )
        await context.send(embed=embed)



# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot) -> None:
    await bot.add_cog(Minecraft(bot))
