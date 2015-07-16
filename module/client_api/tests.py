# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import mock
import copy

from django.test import TestCase
from django.test.client import RequestFactory
from django.test.client import Client
from module.oauth.models import User
from module.setting.models import Design
from .test_data import mock_data
from .api.manager import APIManager


class ClientApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        """
        テスト開始前処理
        """
        # user = User.objects.get(id=mock_data['User']['id'])
        user = mock.Mock()
        user.id = 2
        user.no_cache_all_category_list = []
        user.no_cache_bookmark_list = []
        user.no_cache_page_list = []
        Design.objects.create(user_id=2, image_position='center')

        cls.request_data = mock_data
        cls.manager = APIManager(user, mock_data)

    def setUp(self):
        # self.factory = RequestFactory()
        self.factory = Client()

    def test_delete_duplicate_category_date(self):
        """
        重複データの削除テスト(Category)
        """
        request_data = self.manager.request_data['Category']
        # 重複したデータ削除されていること
        self.assertEqual(len(request_data['insert']), 2)
        self.assertEqual(len(request_data['update']), 0)
        self.assertEqual(len(request_data['delete']), 0)
        # 削除と新規追加のリストに重複して存在した場合はともに削除されていること
        self.assertEqual('2C378211-9438-4660-90C4-67134E831061' in request_data['insert'], False)
        self.assertEqual('2C378211-9438-4660-90C4-67134E831061' in request_data['delete'], False)
        # 更新と新規追加のリストに重複して存在した場合は新規追加が優先されていること
        self.assertEqual('25F3002A-6252-453F-ACFE-25B60BEFE0A1' in request_data['insert'], True)
        self.assertEqual('25F3002A-6252-453F-ACFE-25B60BEFE0A1' in request_data['update'], False)

    def test_delete_duplicate_page_date(self):
        """
        重複データの削除テスト(Page)
        """
        request_data = self.manager.request_data['Page']
        # 重複したデータ削除されていること
        self.assertEqual(len(request_data['insert']), 2)
        self.assertEqual(len(request_data['update']), 0)
        self.assertEqual(len(request_data['delete']), 0)
        # 削除と新規追加のリストに重複して存在した場合はともに削除されていること
        self.assertEqual('07BB482E-6D42-4046-85E1-64BEAAAF6B81' in request_data['insert'], False)
        self.assertEqual('07BB482E-6D42-4046-85E1-64BEAAAF6B81' in request_data['delete'], False)
        # 更新と新規追加のリストに重複して存在した場合は新規追加が優先されていること
        self.assertEqual('BE6E392D-663C-4311-9F2C-15D241D905B3' in request_data['insert'], True)
        self.assertEqual('BE6E392D-663C-4311-9F2C-15D241D905B3' in request_data['update'], False)

    def test_delete_duplicate_bookmark_date(self):
        """
        重複データの削除テスト(Bookmark)
        """
        request_data = self.manager.request_data['Bookmark']
        # 重複したデータ削除されていること
        self.assertEqual(len(request_data['insert']), 3)
        self.assertEqual(len(request_data['update']), 0)
        self.assertEqual(len(request_data['delete']), 0)
        # 削除と新規追加のリストに重複して存在した場合はともに削除されていること
        self.assertEqual('D844421A-38E9-49E6-81A9-2BB689A4DFF1' in request_data['insert'], False)
        self.assertEqual('D844421A-38E9-49E6-81A9-2BB689A4DFF1' in request_data['delete'], False)
        # 更新と新規追加のリストに重複して存在した場合は新規追加が優先されていること
        self.assertEqual('B7F349D6-17D5-45FD-97B6-D2C73C7666FF' in request_data['insert'], True)
        self.assertEqual('B7F349D6-17D5-45FD-97B6-D2C73C7666FF' in request_data['update'], False)

    def test_insert_date(self):
        """
        Clentの新規データを書き込みテスト
        """
        self.manager.run_sync()
        update_response = self.manager.update_response
        self.assertEqual('3DBF2771-6164-4739-A5BA-B1A0F5A9B9FD' in update_response['Bookmark'], True)
        self.assertEqual('B7F349D6-17D5-45FD-97B6-D2C73C7666FF' in update_response['Bookmark'], True)
        self.assertEqual('BEFF4C3E-E14C-49AB-B4FE-A2C03B821093' in update_response['Bookmark'], True)
        self.assertEqual('D844421A-38E9-49E6-81A9-2BB689A4DFF1' in update_response['Bookmark'], False)
        self.assertEqual('25F3002A-6252-453F-ACFE-25B60BEFE0A1' in update_response['Category'], True)
        self.assertEqual('7C9A6189-9F75-4C1B-80B7-24A0EEC8C144' in update_response['Category'], True)
        self.assertEqual('7C9A6189-9F75-4C1B-80B7-24A0EEC8C144' in update_response['Category'], True)
        self.assertEqual('07BB482E-6D42-4046-85E1-64BEAAAF6B81' in update_response['Page'], False)
        self.assertEqual('666E9647-B583-44BB-AD77-9F019CD7659C' in update_response['Page'], True)
        self.assertEqual('BE6E392D-663C-4311-9F2C-15D241D905B3' in update_response['Page'], True)

    def test_update_date(self):
        """
        Clentデータの更新テスト
        """
        pass
        # insert_data = api.insert_date(self.request_data, delete_category_id_list)
        # update_data = api.update_date(self.request_data, insert_data['Page'])
