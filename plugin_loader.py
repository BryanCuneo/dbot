"""Load plugins.

https://lkubuntu.wordpress.com/2012/10/02/writing-a-python-plugin-api/
"""

import os
import imp

MAIN_MODULE = "__init__"


def get_plugins(plugins_dir):
    plugins = []
    possible_plugins = os.listdir(plugins_dir)

    for plugin in possible_plugins:
        location = os.path.join(plugins_dir, plugin)
        if not os.path.isdir(location) or MAIN_MODULE + ".py" not in os.listdir(
            location
        ):
            continue

        info = imp.find_module(MAIN_MODULE, [location])
        plugins.append({"name": plugin, "info": info})
    return plugins


def load_plugin(plugin):
    return imp.load_module(MAIN_MODULE, *plugin["info"])
