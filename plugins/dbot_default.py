from pathlib import Path

from discord.ext import commands

class DbotDefaultCommands(commands.Cog):
    _about_message = """Built with DBot - A plugin-based Discord bot framework
<https://github.com/BryanCuneo/dbot>

Copyright 2018-2022 Bryan Cuneo
https://www.gnu.org/licenses/agpl-3.0.en.html"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dbot(self, ctx):
        await ctx.send(DbotDefaultCommands._about_message)


def setup(bot):
    bot.add_cog(DbotDefaultCommands(bot))
