try:
    import tomllib  # Python 3.11+ - PEP 680
except ImportError:
    import tomli

# Load the config file
with open("config.toml", "rb") as f:
    try:
        config = tomllib.load(f)
    except NameError:
        config = tomli.load(f)


def _about():
    "Information about this bot"
    return config["about_message"]


def define_commands():
    commands = {
        "!about": _about,
    }

    return commands
