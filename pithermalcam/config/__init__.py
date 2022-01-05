from configparser import ConfigParser
from pathlib import Path
from typing import Any, Dict, Tuple


class Config(ConfigParser):
    """
    Global Configuration
    """

    def __init__(self) -> None:
        config_file = Path(__file__).parent / "config.ini"
        super().__init__()
        self.read(config_file)

    def get_server_http_port(self) -> int:
        return self.getint("server", "port")

    def get_image_web_size(self) -> Tuple[int, int]:
        image_size = [int(x) for x in self.get("image", "web_size").split(",")]
        return image_size[0], image_size[1]

    def get_image_size(self) -> Tuple[int, int]:
        image_size = [int(x) for x in self.get("image", "image_size").split(",")]
        return image_size[0], image_size[1]

    def get_colorbar_params(self) -> Dict[str, Any]:
        return dict(self["colorbar"])


config = Config()
