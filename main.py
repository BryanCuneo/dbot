#!/usr/bin/python3
"""A small Discord bot framework."""
import discord

import plugin_loader
from config_loader import config


class Dbot(discord.Client):
    startupMsg = """
DBot - A Discord bot by Bryan Cuneo.
https://github.com/BryanCuneo/dbot

Logged in as: {0.user}
User ID: {0.user.id}
------
"""

    def __init__(self, plugins_dir):
        self.commands = {}

        for p in plugin_loader.get_plugins(plugins_dir):
            print("Loading plugin {}...".format(p["name"]), end="")
            try:
                plugin = plugin_loader.load_plugin(p)
                print(" Done")
            except Exception as e:
                print(" Failed -", e)

            self.commands = {**self.commands, **plugin.define_commands()}

        # initialize discord.Client
        super().__init__()

    @staticmethod
    def _log_command(message):
        """Log commands to the console."""
        print(
            "* Received command - '{}' from {}".format(message.content, message.author)
        )

    @staticmethod
    def _log_response(message):
        """Log a response by the bot."""
        print("* Sending back: {}".format(message))

    async def on_ready(self):
        print(Dbot.startupMsg.format(self))

    async def on_message(self, message):
        """Receive and respond to messages beginning with '!'."""
        # Ignore messages not starting with '!' as well as messages originating
        # from the bot itself
        if not message.content.startswith("!") or message.author == self.user:
            return

        # Check if the command is valid
        try:
            Dbot._log_command(message)
            msg = self.commands[message.content]()
        except KeyError:
            msg = "Invalid command - {}".format(message.content)

        # Mention the user who issued the commands
        msg = "{user} - {msg}".format(user=message.author.mention, msg=msg)

        # Log and send the reply to the specified channel
        Dbot._log_response(msg)
        await message.channel.send(msg)


def main():
    print("Initializing client...")
    client = Dbot(config["plugins_dir"])

    print("Logging in...", end="")
    client.run(config["dbot_access_token"])


if __name__ == "__main__":
    main()
