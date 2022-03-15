#!/usr/bin/python3
"""A small Discord bot framework."""
import os

from discord.ext import commands

from config_loader import config


class Dbot(commands.Bot):
    startupMsg = """
DBot - A Discord bot by Bryan Cuneo.
https://github.com/BryanCuneo/dbot

Logged in as: {0.user}
User ID: {0.user.id}
------
"""

    def __init__(self, plugins_dir):
        # initialize discord.Client
        super().__init__(command_prefix=config["command_prefix"])

        for plugin in os.listdir(plugins_dir):
            if plugin != "__pycache__":
                self.load_extension("plugins.{0}".format(plugin))

    async def on_ready(self):
        print(Dbot.startupMsg.format(self))


def main():
    print("Initializing client...")
    client = Dbot(config["plugins_dir"])

    print("Logging in...", end="")
    client.run(config["dbot_access_token"])


if __name__ == "__main__":
    main()
