import config


def _about():
    "Information about this bot"
    return config.about_message


def define_commands():
    commands = {
        '!about': _about,
    }

    return commands
