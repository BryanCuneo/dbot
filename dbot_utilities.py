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


def config_loader(path, warn_on_blank=True):
    with open(path, "rb") as f:
        try:
            config = tomllib.load(f)
        except NameError:
            config = tomli.load(f)

    # Make sure all config options are present
    if warn_on_blank:
        for key in config.keys():
            if not config[key]:
                logger.warn("{0}: configuration option '{1}' is blank".format(path, key))

    return config
