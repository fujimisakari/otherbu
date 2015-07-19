# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from module.setting.models import Category, Bookmark, Page
from . import BaseController


class InsertController(BaseController):

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
        self.insert_category()
        self.insert_bookmark()
        self.insert_page()

    def result(self):
        """
        結果
        """
        return self.response_data

    def insert_category(self):
        """
        カテゴリデータの新規追加
        """
        cateogry_id_list = []
        create_cateogry_data = []

        for data_id, data in self.request_data['Category']['insert'].items():
            data = Category(user_id=int(self.user.id), mobile_id=data['id'], name=data['name'], angle=int(data['angle']), sort=int(data['sort']),
                            color_id=int(data['color_id']), tag_open=int(data['tag_open']), sync_flag=False)
            create_cateogry_data.append(data)
            cateogry_id_list.append(data_id)

        Category.objects.bulk_create(create_cateogry_data)
        inserted_category = Category.objects.filter(mobile_id__in=cateogry_id_list)
        self.response_data['Category'] = {category.mobile_id: category.to_dict() for category in inserted_category}

    def insert_bookmark(self):
        """
        ブックマークの新規追加
        """
        category_map = self.response_data['Category']
        bookmark_id_list = []
        create_bookmark_data = []
        for data_id, data in self.request_data['Bookmark']['insert'].items():
            category_id = category_map[data['category_id']]['id'] if category_map.get(data['category_id'], False) else data['category_id']
            bookmark = Bookmark(user_id=int(self.user.id), mobile_id=data['id'], category_id=category_id, name=data['name'],
                                url=data['url'], sort=int(data['sort']), sync_flag=False)
            create_bookmark_data.append(bookmark)
            bookmark_id_list.append(data_id)

        Bookmark.objects.bulk_create(create_bookmark_data)
        inserted_bookmark = Bookmark.objects.filter(mobile_id__in=bookmark_id_list)
        self.response_data['Bookmark'] = {bookmark.mobile_id: bookmark.to_dict() for bookmark in inserted_bookmark}

    def insert_page(self):
        """
        ページの新規追加
        """
        category_map = self.response_data['Category']
        page_id_list = []
        create_page_data = []
        for data_id, data in self.request_data['Page']['insert'].items():
            # pageにClientで作成されたIDを保持してる場合は,DBで生成されたIDに差し替える
            self._update_category_id_by_page_data(data, category_map, self.delete_category_id_list)

            data = Page(user_id=int(self.user.id), mobile_id=data['id'], name=data['name'], category_ids_str=data['category_ids_str'],
                        angle_ids_str=data['angle_ids_str'], sort_ids_str=data['sort_ids_str'], sync_flag=False)

            create_page_data.append(data)
            page_id_list.append(data_id)

        Page.objects.bulk_create(create_page_data)
        inserted_page = Page.objects.filter(mobile_id__in=page_id_list)
        self.response_data['Page'] = {page.mobile_id: page.to_dict() for page in inserted_page}
