# -*- coding: utf-8 -*-

import socket
import os
import re
from settings.private_config import *

HOSTNAME = socket.gethostname()
if HOSTNAME == PUBLIC_HOSTNAME:
    # 本番サーバー
    # 本番サーバー内で本番環境とdev環境を切り分ける
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    if re.search(DEV_DIRECTORY, ROOT_PATH):
        from settings.dev_settings import *
    else:
        from settings.base_settings import *
else:
    # local環境
    from settings.dev_settings import *
