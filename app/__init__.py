from typing import Awaitable, Callable

from app.utils.classes import Config, ConfigLoader

version = "1.0.0"

config_loader = ConfigLoader()
config: Config = config_loader.config
