from module.setting.models import Bookmark, Category, DeleteManager, Page

from . import BaseController


class DeleteController(BaseController):

    def init_setup(self, **kw):
        """
        初期設定
        """
        self.user = kw['user']
        self.request_data = kw['request_data']
        self.response_data = kw['response_data']

    def run(self):
        """
        実行
        """
        # クライアント変更分を更新
        self._delete(Category, self.request_data['Category']['delete'])
        self._delete(Bookmark, self.request_data['Bookmark']['delete'])
        self._delete(Page, self.request_data['Page']['delete'])

        # サーバー側の変更分を更新
        try:
            delete_manage = DeleteManager.objects.get(user_id=self.user.id)
        except DeleteManager.DoesNotExist:
            return

        self.response_data['Bookmark'] = self._get_delete_ids(delete_manage.bookmark)
        self.response_data['Category'] = self._get_delete_ids(delete_manage.category)
        self.response_data['Page'] = self._get_delete_ids(delete_manage.page)
        delete_manage.reset()

    def result(self):
        """
        結果
        """
        return self.response_data

    def _get_delete_ids(self, ids_str):
        if ids_str:
            return str(ids_str).split(',')
        else:
            return []

    def _delete(self, obj, data):
        delete_id_list = [data_id for data_id, _ in data.items()]
        if delete_id_list:
            obj.objects.filter(id__in=delete_id_list).delete()
