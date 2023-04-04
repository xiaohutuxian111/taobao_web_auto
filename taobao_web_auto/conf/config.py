"""
@FileName：config.py
@Author：stone
@Time：2023/4/4 17:59
@Description：项目基础的配置文件
"""
import os.path

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 配置文件路径
CONF_PATH = os.path.join(ROOT_PATH, 'conf')
# log路径
LOG_PATH = os.path.join(ROOT_PATH, 'log')

if __name__ == '__main__':
    print(ROOT_PATH)
