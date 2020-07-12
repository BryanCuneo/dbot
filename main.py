#!/usr/bin/python3
"""A small Discord bot framework."""
import discord

import default_commands
import plugin_loader

try:
    import config
except ImportError:
    error = """
ERROR: Could not find configuration file 'config.py'
Please see the included 'config_template.py'
"""
    print(error)
    exit()

# Load plugins
commands = default_commands.define_commands()

for p in plugin_loader.get_plugins(config.plugins_dir):
    print('Loading plugin {}...'.format(p['name']))
    plugin = plugin_loader.load_plugin(p)

    commands = {**commands, **plugin.define_commands()}

# Instantiate Discord client
client = discord.Client()


def log_command(message):
    """Log commands to the console."""
    print('* Received command - \'{}\' from {}'.format(
        message.content,
        message.author
    ))


def log_response(message):
    """Log a response by the bot."""
    print('* Sending back: {}'.format(message))


@client.event
async def on_message(message):
    """Receive and respond to messages beginning with '!'."""
    # Ignore messages not starting with '!' as well as messages originating
    # from the bot itself
    if not message.content.startswith('!') or message.author == client.user:
        return

    log_command(message)

    # Check if the command is valid
    try:
        msg = commands[message.content]()
    except KeyError:
        msg = 'Invalid command - {}'.format(message.content)

    # Mention the user who issued the commands
    msg = '{user} - {msg}'.format(
        user=message.author.mention,
        msg=msg
    )

    # Log and send the reply to the specified channel
    log_response(msg)
    await message.channel.send(msg)


@client.event
async def on_ready():
    """Display startup message."""
    startupMsg = """
DBot - A Discord bot by Bryan Cuneo.
https://github.com/BryanCuneo/dbot

Logged in as: {}
User ID: {}
------
"""
    print(startupMsg.format(client.user.name, client.user.id))

print('Logging in...')
client.run(config.dbot_access_token)
