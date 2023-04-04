"""
@FileName：test_logging.py
@Author：stone
@Time：2023/4/4 18:17
@Description：
"""
import pytest
from taobao_web_auto.utils.logging import loggings


class Test_Logging:
    def test_info(self):
        loggings.info("info通知信息")
        assert False

    def test_debug(self):
        loggings.debug("debug日志信息")
        assert False

    def test_warning(self):
        loggings.warning("warning警告信息")
        assert False

    def test_error(self):
        loggings.error("error错误信息")
        assert False
