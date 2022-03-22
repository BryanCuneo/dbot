# Plugins
Plugins provide functionality to your bot via Discord.py [Extensions](https://discordpy.readthedocs.io/en/stable/ext/commands/extensions.html) and [Cogs](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html#ext-commands-cogs) that are loaded automatically at runtime.

## Single-File
A self-contained extension file. [dbot_default.py](/plugins/dbot_default.py) is a very basic single-file plugin that registers a simple command. 

## Multi-file
If you wish to spread your plugin across multiple files, you can do so via subfolders within your plugins directory like so:

```
dbot/
├─ plugins/
│  ├─ dbot_default.py
│  ├─ multi_file/
│  │  ├─ __init__.py
│  │  ├─ extra_file.py
```

`__init__.py` is the entry point for the extension and is required.


# More sample plugins (including multi-line) coming soon™.
