"""
@FileName：logging.py
@Author：stone
@Time：2023/4/4 17:49
@Description：
"""
import os.path
import time

from loguru import logger

log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log')


class Loggings(object):
    """使用loguru实现生成日志"""
    t_str = time.strftime("%Y-%m-%d")
    logger.add(f"{log_path}/selenium_{t_str}.log", rotation="500MB", encoding="utf-8", enqueue=True,
               retention="10 days")

    __instance = None

    #  d单例模式，防止重复创建日志句柄
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def info(self, msg):
        return logger.info(msg)

    def debug(self, msg):
        return logger.debug(msg)

    def warning(self, msg):
        return logger.warning(msg)

    def error(self, msg):
        return logger.error(msg)


loggings = Loggings()



