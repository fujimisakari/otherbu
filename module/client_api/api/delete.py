# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from module.setting.models import DeleteManager
from . import BaseController


class DeleteController(BaseController):

    def init_setup(self, **kw):
        """
        初期設定
        """
        self.user = kw['user']
        self.request_data = kw['request_data']
        self.response_data = kw['response_data']
        self.delete_category_id_list = kw['delete_category_id_list']

    def run(self):
        """
        実行
        """
        try:
            delete_manage = DeleteManager.objects.get(user_id=self.user.id)
        except DeleteManager.DoesNotExist:
            return

        self.response_data['Bookmark'] = str(delete_manage.bookmark).split(',')
        self.response_data['Category'] = str(delete_manage.category).split(',')
        self.response_data['Page'] = str(delete_manage.page).split(',')

    def result(self):
        """
        結果
        """
        return self.response_data
