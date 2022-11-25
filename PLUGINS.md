# Plugins
Plugins provide functionality to your bot via [Extensions](https://docs.pycord.dev/en/stable/ext/commands/extensions.html) and [Cogs](https://docs.pycord.dev/en/stable/ext/commands/cogs.html) that are loaded automatically at runtime.

## Single-File
A self-contained extension file. [dice_roller.py](/plugins/dice_roller.py) is a very basic single-file plugin that registers a simple command.

## Multi-file
If you wish to spread your plugin across multiple files, you can do so via subfolders within your plugins directory like so:

```
dbot/
├─ plugins/
│  ├─ multi_file_plugin/
│  │  ├─ __init__.py
│  │  ├─ do_stuff.py
|  |  ├─ config.toml
```

Check out the [recurring message scheduler](/plugins/recurring_messages) for an example of a multi-file plugin.

`__init__.py` is the required entry point for multi-file plugins.
