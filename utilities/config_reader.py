import configparser
from constants import ROOT_PATH

_abs_path = f"{ROOT_PATH}/configs/app_config.ini"
_config = configparser.RawConfigParser()
_config.read(_abs_path)


class AppConfig:
    url = _config.get('app_data', 'url')
    browser_id = _config.get('browser_data', 'browser_id')
