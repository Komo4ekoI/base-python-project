import os
import sys
from dataclasses import dataclass

from dotenv import load_dotenv, find_dotenv

from app.utils.custom_logger import CustomLogger


@dataclass
class AppConfig:
    debug_mode: bool


class Config:
    def __init__(self, app: AppConfig):
        self.app = app


class ConfigLoader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    @classmethod
    def _load_config(cls):
        cls.config = cls._parse_config()

    @staticmethod
    def _parse_config() -> Config:
        logger = CustomLogger("ConfigLoader")
        logger.info("Loading config")

        try:
            load_dotenv(find_dotenv())

            app = AppConfig(
                debug_mode=os.getenv("DEBUG_MODE", "false").lower() == "true",
            )

            return Config(app)
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            sys.exit(1)
