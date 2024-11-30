import sys
import os

# 将项目目录加入到 Python 路径中
project_home = '/home/OvOTian/json_tool'
if project_home not in sys.path:
    sys.path.append(project_home)

# 导入 Flask 应用
from app import app as application  # 假设你的 Flask 实例名为 app
