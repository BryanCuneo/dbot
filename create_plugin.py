"""Create the filestructure for a new plugin"""
import sys
from pathlib import Path

from dbot_utilities import load_config

init_file_content = """from pathlib import Path

import discord

from dbot_utilities import load_config, schedule_task


class {0}(discord.Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config


def setup(bot):
    config = load_config(Path(__file__).parent.joinpath("config.toml"))
    bot.add_cog({0}(bot, config))
"""


def main():
    if len(sys.argv) > 1:
        project_name = " ".join(sys.argv[1:])
    else:
        project_name = input("Enter plugin name: ")
    print("\nBuilding new plugin folder for", project_name)
    print("-" * (31 + len(project_name)))

    clean_name = "".join(
        char for char in project_name if (char.isalnum() or char in "_- ")
    )
    class_name = clean_name.replace(" ", "")
    folder_name = clean_name.lower().replace(" ", "_")
    folder_path = Path(config["plugins_dir"], folder_name)
    try:
        print("Creating base directory: {0}...".format(folder_path), end="")
        folder_path.mkdir(parents=True, exist_ok=False)
        print(" Done")
    except FileNotFoundError:
        print(" Error: Directory already exists. Exiting.")
        exit

    print("Creating files...", end="")
    # Create an __init__.py file
    init_filepath = Path(folder_path, "__init__.py")
    with open(init_filepath, "x") as f:
        f.write(init_file_content.format(class_name))

    # Create an empty config file
    config_filepath = Path(folder_path, "config.toml")
    with open(config_filepath, "x") as f:
        f.write("")
    print(" Done\n\nSuccess")


if __name__ == "__main__":
    config = load_config()
    main()
