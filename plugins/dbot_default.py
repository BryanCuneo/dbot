from discord.ext import commands

from config_loader import config


class DbotDefault(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        await ctx.send(config["about_message"])


def setup(bot):
    bot.add_cog(DbotDefault(bot))
