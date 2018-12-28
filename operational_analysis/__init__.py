__version__ = "1.0"

import json
import logging
import logging.config
import os


def setup_logging(default_path='logging.json',
                  default_level=logging.WARN,
                  env_key='LOG_CFG'):
    """Setup logging configuration """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


setup_logging()
