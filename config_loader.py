import logging

try:
    import tomllib  # Python 3.11+ - PEP 680
except ImportError:
    import tomli

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Config Loader")

with open("config.toml", "rb") as f:
    try:
        config = tomllib.load(f)
    except NameError:
        config = tomli.load(f)

# Make sure all config options are present
for key in config.keys():
    if not config[key] or (config[key].isspace() and key != "channel_id"):
        logger.warn("Configuration option '{0}' is blank".format(key))
