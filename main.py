"""A small Discord bot framework."""
import logging
from pathlib import Path

from discord.ext import commands

from config_loader import config


class Dbot(commands.Bot):
    startupMsg = """
DBot - A Discord bot by Bryan Cuneo.
https://github.com/BryanCuneo/dbot

Logged in as: {0}
User ID: {0.id}
------
"""

    def __init__(self, plugins_dir):
        # initialize discord.Client
        super().__init__(command_prefix=config["command_prefix"])

        for plugin in Path(plugins_dir).iterdir():
            if plugin.stem != "__pycache__":
                logger.info("Loading plugin: " + str(plugin))
                self.load_extension("plugins." + plugin.stem)

    async def on_ready(self):
        print(Dbot.startupMsg.format(self.user))

def main():
    logger.info("Initializing client...")
    client = Dbot(config["plugins_dir"])
    client.run(config["dbot_access_token"])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("DBot")
    main()
