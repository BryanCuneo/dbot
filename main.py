"""A small Discord bot framework."""
import logging
from pathlib import Path

from discord.ext import commands

from dbot_utilities import config_loader


class Dbot(commands.Bot):
    _startupMsg = """
Built with DBot - A plugin-based Discord bot framework
<https://github.com/BryanCuneo/dbot>

Copyright 2018-2022 Bryan Cuneo
https://www.gnu.org/licenses/agpl-3.0.en.html

Logged in as: {0}
User ID: {0.id}
------"""

    def __init__(self, plugins_dir):
        # initialize discord.Client
        super().__init__(command_prefix=config["command_prefix"])

        for plugin in Path(plugins_dir).iterdir():
            if plugin.stem != "__pycache__":
                logger.info("Loading plugin: " + str(plugin))
                self.load_extension("plugins." + plugin.stem)

    async def on_ready(self):
        print(Dbot._startupMsg.format(self.user))

def main():
    logger.info("Initializing client...")
    client = Dbot(config["plugins_dir"])
    client.run(config["dbot_access_token"])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("DBot")

    config = config_loader(Path(__file__).parent.joinpath("config.toml"))

    main()
