"""
=============================
Author:sangshen
time:2022/2/15 
E-mail:928857196@qq.com 
=============================
"""

from configparser import ConfigParser
from common.Handle_path import CONF_DIR
import os


class Config(ConfigParser):

    def __init__(self, config_file):
        super().__init__()
        self.read(config_file, encoding="utf-8")


conf = Config(os.path.join(CONF_DIR, "config.ini"))

# if __name__ == "__main__":
# conf = ConfigParser()
# conf.read(r"D:\nmb_learn_2022\s2022_02_15\config.ini", encoding="utf-8")
#
# conf = Config(r"D:\nmb_learn_2022\s2022_02_15\config.ini")
# name = conf.get("logging", "name")
# level = conf.get("logging", "level")
# filename = conf.get("logging", "filename")
# sh_level = conf.get("logging", "sh_level")
# fh_level = conf.get("logging", "fh_level")
# print(name, level, filename, sh_level, fh_level)
