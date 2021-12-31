from configparser import ConfigParser
from pathlib import Path
from typing import Tuple


class Config(ConfigParser):
    """
    Global Configuration
    """

    def __init__(self) -> None:
        config_file = Path(__file__).parent / "config.ini"
        super().__init__()
        self.read(config_file)

    def get_image_web_size(self) -> Tuple[int, int]:
        image_size = [int(x) for x in self.get("image", "web_size").split(",")]
        return image_size[0], image_size[1]

    def get_image_size(self) -> Tuple[int, int]:
        image_size = [int(x) for x in self.get("image", "image_size").split(",")]
        return image_size[0], image_size[1]

config = Config()
