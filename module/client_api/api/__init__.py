# -*- coding: utf-8 -*-

import datetime

from abc import ABCMeta, abstractmethod


class BaseController:
    __metaclass__ = ABCMeta

    @abstractmethod
    def init_setup(self, **kw):
        """
        初期設定
        """
        pass

    @abstractmethod
    def run(self):
        """
        実行
        """
        pass

    @abstractmethod
    def result(self):
        """
        結果
        """
        pass

    def _update_at(self, update_at_str):
        date = update_at_str.split(',')
        date = [int(x) for x in date]
        update_at = datetime.datetime(date[0], date[1], date[2], date[3], date[4], date[5])
        return update_at
