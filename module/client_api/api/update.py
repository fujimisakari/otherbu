# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from module.setting.models import Category, Bookmark, Page, Design
from . import BaseController


class UpdateController(BaseController):

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
        self.update_category()
        self.update_bookmark()
        self.update_page()
        self.update_design()
        self.update_user()

    def result(self):
        """
        結果
        """
        return self.response_data

    def update_user(self):
        """
        ユーザーの更新
        """
        update_user = self.request_data['User']
        page_id = self.request_data['User']['page_id']
        if self._update_at(update_user['updated_at']) > self.user.updated_at:
            # クライアント側で更新があった場合
            page_map = self.response_data['Page']
            if page_map.get(page_id, False):
                self.user.page_id = page_map.get(page_id)
            else:
                self.user.page_id = page_id
            self.user.use_mobile = True
            self.user.save()
        elif self.user.sync_flag:
            # クライアント側の更新がなくサーバー側のみ更新した場合
            self.user.sync_flag = False
            self.user.save()
            self.response_data['User'] = self.user.to_dict()

    def update_category(self):
        """
        カテゴリの更新
        """
        # 更新データの整形
        request_data = self.request_data['Category']['update']
        exclude_data = []
        server_sync_data = {x.id: x for x in self.user.no_cache_all_category_list if x.sync_flag}
        self._clean_up_update_data(server_sync_data, request_data, self.response_data['Category'], exclude_data)

        # クライアント変更分を更新
        for data_id, sync_data in request_data.items():
            if data_id not in exclude_data:
                try:
                    category = Category.objects.get(id=data_id)
                    category.update_sync(sync_data)
                except Category.DoesNotExist:
                    pass

        # サーバーの同期対象はすべてOffる
        Category.objects.filter(user_id=self.user.id).update(sync_flag=False)

    def update_bookmark(self):
        """
        ブックマークの更新
        """
        # 更新データの整形
        request_data = self.request_data['Bookmark']['update']
        exclude_data = []
        server_sync_data = {x.id: x for x in self.user.no_cache_bookmark_list if x.sync_flag}
        self._clean_up_update_data(server_sync_data, request_data, self.response_data['Bookmark'], exclude_data)

        # クライアント変更分を更新
        for data_id, sync_data in request_data.items():
            if data_id not in exclude_data:
                try:
                    category_map = self.response_data['Category']
                    if category_map.get(sync_data['category_id'], False):
                        category_id = category_map[sync_data['category_id']]['id']
                    else:
                        category_id = sync_data['category_id']
                    bookmark = Bookmark.objects.get(id=data_id)
                    bookmark.update_sync(sync_data, category_id)
                except Bookmark.DoesNotExist:
                    pass

        # サーバーの同期対象はすべてOffる
        Bookmark.objects.filter(user_id=self.user.id).update(sync_flag=False)

    def update_page(self):
        """
        ページの更新
        """
        # 更新データの整形
        request_data = self.request_data['Page']['update']
        exclude_data = []
        server_sync_data = {x.id: x for x in self.user.no_cache_page_list if x.sync_flag}
        self._clean_up_update_data(server_sync_data, request_data, self.response_data['Page'], exclude_data)

        # クライアント変更分を更新
        for data_id, sync_data in request_data.items():
            if data_id not in exclude_data:
                try:
                    category_map = self.response_data['Category']
                    self._update_category_id_by_page_data(sync_data, category_map, self.delete_category_id_list)
                    page = Page.objects.get(id=data_id)
                    page.update_sync(sync_data)
                except Page.DoesNotExist:
                    pass

        # サーバーの同期対象はすべてOffる
        Page.objects.filter(user_id=self.user.id).update(sync_flag=False)

    def update_design(self):
        """
        デザインの更新
        """
        design = Design.objects.get(user_id=self.user.id)
        update_design = self.request_data['Design']
        if update_design:
            # クライアント側で更新があった場合
            if self._update_at(update_design['updated_at']) > design.updated_at:
                design.category_back_color = update_design['category_back_color']
                design.link_color = update_design['link_color']
                design.save()
        elif design.sync_flag:
            # クライアント側の更新がなくサーバー側のみ更新した場合
            design.sync_flag = False
            design.save()
            self.response_data['Design'] = design.to_dict()

    def _clean_up_update_data(self, server_sync_data, request_data, response_data, exclude_data):
        """
        サーバー側とクライアント側の更新でどちらを優先させるか判定
        """
        for data_id, data in server_sync_data.items():
            key = data.mobile_id if data.mobile_id else data_id
            if request_data.get(data_id, False):
                # サーバーとクライアントの更新がかぶってサーバーの方が新しかった場合
                if data.updated_at > self._update_at(request_data['updated_at']):
                    response_data[key] = data.to_dict()
                    # クライアントの更新対象から省く
                    exclude_data.append(data_id)
            else:
                # サーバーのみの更新の場合
                response_data[key] = data.to_dict()
