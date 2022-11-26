import asyncio
from datetime import datetime, timezone

from discord.ext import tasks

try:
    import tomllib  # Python 3.11+ - PEP 680
except ImportError:
    import tomli as tomllib


def _time_diff(time_str):
    format_str = "%H:%M:%S"
    now = datetime.strftime(datetime.now(timezone.utc), format_str)
    tdelta = datetime.strptime(time_str, format_str) - datetime.strptime(
        now, format_str
    )

    return tdelta.seconds


def load_config(path="./config.toml", warn_on_blank=True):
    with open(path, "rb") as f:
        config = tomllib.load(f)

    return config


# reminder = {
#     "message": "Hello",
#     "recur_on": ["sunday", "monday", "tuesday", "wednsday", "thursday", "friday", "saturday"],
#     "time": "17:30:00"
#     "channel": 1234
# }
def schedule_task(bot, reminder):
    """Create a function to run every 24 hours that will send a message in a
    given channel on specified days.
    """

    # Specify to run once a day
    @tasks.loop(hours=24)
    async def fun():
        channel = bot.get_channel(reminder["channel"])
        # If the current day is listed in the reminder's recur_on field, send
        # the message to the specified channel.  Otherwise, do nothing
        today = datetime.now().strftime("%A").lower()
        if today in (day.lower() for day in reminder["recur_on"]):
            timestamp = datetime.now(timezone.utc).strftime("[%a %b %d, %H:%M:%S]")
            print(
                '{0} Running scheduled task: "{message}" in channel {channel}'.format(
                    timestamp, **reminder
                )
            )
            await channel.send(reminder["message"])

    # Wait until the specified time to run
    @fun.before_loop
    async def before_fun():
        seconds = _time_diff(reminder["time"])
        await asyncio.sleep(seconds)

    print(
        '  * Registering scheduled task: Say "{message}" in channel {channel} at {time}UTC on:\n    {recur_on}'.format(
            **reminder
        )
    )
    fun.start()
