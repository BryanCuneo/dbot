from discord.ext import commands, tasks

from dbot_utilities import config_loader, task_scheduler


class RecurringMessages(commands.Cog):
    __config = config_loader(Path(__file__).parent.joinpath("config.toml"))

    def __init__(self, bot, config):
        self.bot = bot
        self.config = config

        # Configurable reminders
        for reminder in self.config["reminders"]:
            task = task_scheduler(self.bot, reminder)
            task.start()

        # Hardcoded reminder
        reminder = {
            "message": "I'm hard coded.",
            "recur_on": ["friday", "saturday", "sunday"],
            "time": "12:00:00",
            "channel": 123,
        }
        task = task_scheduler(self.bot, reminder)
        task.start()


def setup(bot):
    config = config_loader(Path(__file__).parent.joinpath("config.toml"))

    bot.add_cog(RecurringMessages(bot, config))
