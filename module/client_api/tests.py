# -*- coding: utf-8 -*-

import copy

from django.test import TestCase
from django.test.client import RequestFactory
from django.test.client import Client

from .test_data import mock_data
from .views import sync
from . import api


class ClientApiTest(TestCase):

    def setUp(self):
        self.request_data = mock_data
        # self.factory = RequestFactory()
        self.factory = Client()

    def test_delete_duplicate_category_date(self):
        """
        重複データの削除テスト(Category)
        """
        self.delete_category_id_list = [category_id for category_id, _ in self.request_data['Category']['delete'].items()]
        self.request_data['Category'] = api.delete_duplicate_date(self.request_data['Category'])
        # 重複したデータ削除されていること
        self.assertEqual(len(self.request_data['Category']['insert']), 2)
        self.assertEqual(len(self.request_data['Category']['update']), 0)
        self.assertEqual(len(self.request_data['Category']['delete']), 0)
        # 削除と新規追加のリストに重複して存在した場合はともに削除されていること
        self.assertEqual('2C378211-9438-4660-90C4-67134E831061' in self.request_data['Category']['insert'], False)
        self.assertEqual('2C378211-9438-4660-90C4-67134E831061' in self.request_data['Category']['delete'], False)
        # 更新と新規追加のリストに重複して存在した場合は新規追加が優先されていること
        self.assertEqual('25F3002A-6252-453F-ACFE-25B60BEFE0A1' in self.request_data['Category']['insert'], True)
        self.assertEqual('25F3002A-6252-453F-ACFE-25B60BEFE0A1' in self.request_data['Category']['update'], False)

    def test_delete_duplicate_page_date(self):
        """
        重複データの削除テスト(Page)
        """
        self.request_data['Page'] = api.delete_duplicate_date(self.request_data['Page'])
        # 重複したデータ削除されていること
        self.assertEqual(len(self.request_data['Page']['insert']), 2)
        self.assertEqual(len(self.request_data['Page']['update']), 0)
        self.assertEqual(len(self.request_data['Page']['delete']), 0)
        # 削除と新規追加のリストに重複して存在した場合はともに削除されていること
        self.assertEqual('07BB482E-6D42-4046-85E1-64BEAAAF6B81' in self.request_data['Page']['insert'], False)
        self.assertEqual('07BB482E-6D42-4046-85E1-64BEAAAF6B81' in self.request_data['Page']['delete'], False)
        # 更新と新規追加のリストに重複して存在した場合は新規追加が優先されていること
        self.assertEqual('BE6E392D-663C-4311-9F2C-15D241D905B3' in self.request_data['Page']['insert'], True)
        self.assertEqual('BE6E392D-663C-4311-9F2C-15D241D905B3' in self.request_data['Page']['update'], False)

    def test_delete_duplicate_bookmark_date(self):
        """
        重複データの削除テスト(Bookmark)
        """
        self.request_data['Bookmark'] = api.delete_duplicate_date(self.request_data['Bookmark'])
        # 重複したデータ削除されていること
        self.assertEqual(len(self.request_data['Bookmark']['insert']), 3)
        self.assertEqual(len(self.request_data['Bookmark']['update']), 0)
        self.assertEqual(len(self.request_data['Bookmark']['delete']), 0)
        # 削除と新規追加のリストに重複して存在した場合はともに削除されていること
        self.assertEqual('D844421A-38E9-49E6-81A9-2BB689A4DFF1' in self.request_data['Bookmark']['insert'], False)
        self.assertEqual('D844421A-38E9-49E6-81A9-2BB689A4DFF1' in self.request_data['Bookmark']['delete'], False)
        # 更新と新規追加のリストに重複して存在した場合は新規追加が優先されていること
        self.assertEqual('B7F349D6-17D5-45FD-97B6-D2C73C7666FF' in self.request_data['Bookmark']['insert'], True)
        self.assertEqual('B7F349D6-17D5-45FD-97B6-D2C73C7666FF' in self.request_data['Bookmark']['update'], False)

    def test_insert_date(self):
        """
        Clentの新規データを書き込みテスト
        """
        delete_category_id_list = ['2C378211-9438-4660-90C4-67134E831061']
        insert_data = api.insert_date(self.request_data, delete_category_id_list)
        self.assertEqual('3DBF2771-6164-4739-A5BA-B1A0F5A9B9FD' in insert_data['Bookmark'], True)
        self.assertEqual('B7F349D6-17D5-45FD-97B6-D2C73C7666FF' in insert_data['Bookmark'], True)
        self.assertEqual('BEFF4C3E-E14C-49AB-B4FE-A2C03B821093' in insert_data['Bookmark'], True)
        self.assertEqual('D844421A-38E9-49E6-81A9-2BB689A4DFF1' in insert_data['Bookmark'], False)
        self.assertEqual('25F3002A-6252-453F-ACFE-25B60BEFE0A1' in insert_data['Category'], True)
        self.assertEqual('7C9A6189-9F75-4C1B-80B7-24A0EEC8C144' in insert_data['Category'], True)
        self.assertEqual('7C9A6189-9F75-4C1B-80B7-24A0EEC8C144' in insert_data['Category'], True)
        self.assertEqual('07BB482E-6D42-4046-85E1-64BEAAAF6B81' in insert_data['Page'], False)
        self.assertEqual('666E9647-B583-44BB-AD77-9F019CD7659C' in insert_data['Page'], True)
        self.assertEqual('BE6E392D-663C-4311-9F2C-15D241D905B3' in insert_data['Page'], True)

    def test_update_date(self):
        """
        Clentデータの更新テスト
        """
        pass
        # delete_category_id_list = ['2C378211-9438-4660-90C4-67134E831061']
        # insert_data = api.insert_date(self.request_data, delete_category_id_list)
        # update_data = api.update_date(self.request_data, insert_data['Page'])
