"""
=============================
Author:sangshen
time:2022/2/14 
E-mail:928857196@qq.com 
=============================
"""
'''
为了避免程序中创建多个日志收集器而带导致日志重复记录
那么我们可以只创建一个日志收集器，别的模块使用时都导入这个日志收集器

'''

import logging
from common.Handle_config import Config
from common.Handle_path import LOG_DIR, CONF_DIR
import os

conf = Config(os.path.join(CONF_DIR, "config.ini"))


def create_log(name=conf.get("logging", "name"), level=conf.get("logging", "level"),
               filename=os.path.join(LOG_DIR, conf.get("logging", "filename")),
               sh_level=conf.get("logging", "sh_level"),
               fh_level=conf.get("logging", "fh_level")):
    # 第一步:创建日志收集器
    log = logging.getLogger(name)

    # 第二步:创建日志收集等级
    log.setLevel(level)

    # 第三步:设置输出渠道
    # 3.1 输出到文件的配置
    fh = logging.FileHandler(filename, encoding="utf-8")
    fh.setLevel(fh_level)
    log.addHandler(fh)

    # 3.2 输出到控制台的配置
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)

    # 第四步:设置日志输出格式
    # 4.设置日志输出的等级
    formats = "%(asctime)s--%(filename)s--%(levelname)s--:%(message)s"
    # 创建格式对象
    log_format = logging.Formatter(formats)
    # 为输出渠道设置输出格式
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)

    # 返回一个日志收集器
    return log


my_log = create_log(
    name=conf.get("logging", "name"),
    level=conf.get("logging", "level"),
    filename=os.path.join(LOG_DIR, conf.get("logging", "filename")),
    sh_level=conf.get("logging", "sh_level"),
    fh_level=conf.get("logging", "fh_level"),
)
