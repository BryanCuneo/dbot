import asyncio
import logging
from datetime import datetime
from pathlib import Path

from discord.ext import tasks

try:
    import tomllib  # Python 3.11+ - PEP 680
except ImportError:
    import tomli

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _time_diff(time_str):
    format_str = "%H:%M:%S"
    now = datetime.strftime(datetime.utcnow(), format_str)
    tdelta = datetime.strptime(time_str, format_str) - datetime.strptime(
        now, format_str
    )

    return tdelta.seconds


def load_config(path="./config.toml", warn_on_blank=True):
    with open(path, "rb") as f:
        try:
            config = tomllib.load(f)
        except NameError:
            config = tomli.load(f)

    # Make sure all config options are present
    if warn_on_blank:
        for key in config.keys():
            if not config[key]:
                logger.warn(
                    "{0}: configuration option '{1}' is blank".format(path, key)
                )

    return config


# reminder = {
#     "message": "Hello",
#     "recur_on": ["sunday", "monday", "tuesday", "wednsday", "thursday", "friday", "saturday"],
#     "time": "17:30:00"
#     "channel": 1234
# }
def schedule_task(bot, reminder):
    @tasks.loop(hours=24)
    async def fun():
        channel = bot.get_channel(reminder["channel"])
        today = datetime.now().strftime("%A").lower()
        if today in (day.lower() for day in reminder["recur_on"]):
            await channel.send(reminder["message"])

    @fun.before_loop
    async def before_fun():
        seconds = _time_diff(reminder["time"])
        await asyncio.sleep(seconds)

    return fun