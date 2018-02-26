from .delete import DeleteController
from .insert import InsertController
from .update import UpdateController


class APIManager(object):

    def __init__(self, user, request_data):
        """
        初期設定
        """
        self.user = user
        self.request_data = request_data
        self.update_response = {'Category': {}, 'Bookmark': {}, 'Page': {}, 'User': {}, 'Design': {}}
        self.delete_response = {'Category': [], 'Bookmark': [], 'Page': []}
        self.delete_category_id_list = [category_id for category_id, _ in self.request_data['Category']['delete'].items()]
        # 追加や更新、削除などで重複データがあれば解消させる(優先順位: 削除 > 更新 > 追加)
        self.delete_duplicate_date(self.request_data['Category'])
        self.delete_duplicate_date(self.request_data['Page'])
        self.delete_duplicate_date(self.request_data['Bookmark'])

    def run_sync(self):
        """
        同期実行

        # 追加や更新、削除などで重複データがあれば解消させる(優先順位: 削除 > 更新 > 追加)
        """
        run_data = [{'class': InsertController,
                     'kw': {'user': self.user,
                            'request_data': self.request_data,
                            'response_data': self.update_response,
                            'delete_category_id_list': self.delete_category_id_list}},
                    {'class': UpdateController,
                     'kw': {'user': self.user,
                            'request_data': self.request_data,
                            'response_data': self.update_response,
                            'delete_category_id_list': self.delete_category_id_list}},
                    {'class': DeleteController,
                     'kw': {'user': self.user,
                            'request_data': self.request_data,
                            'response_data': self.delete_response}}]
        for data in run_data:
            c = data['class']()
            c.init_setup(**data['kw'])
            c.run()

    def delete_duplicate_date(self, request_data):
        """
        重複しているデータを消す
        """
        # 削除するデータIDを取得
        delete_id_list = [k for k, _ in request_data['delete'].items()]

        # 削除するデータは更新リストには存在しないようにする
        self.request_data['update'] = {k: v for k, v in request_data['update'].items() if k not in self.delete_category_id_list}

        # 新規追加するデータが更新リストに存在している場合は、更新リストの情報を新規追加として扱う
        update_dict = {}
        for data_id, data in request_data['update'].items():
            if data_id in request_data['insert']:
                request_data['insert'][data_id] = data
            else:
                update_dict[data_id] = data
        request_data['update'] = update_dict

        # 新規追加と削除のリストに重複して存在するデータは、共に消す
        for data_id in delete_id_list:
            if data_id in request_data['insert']:
                del request_data['insert'][data_id]
                del request_data['delete'][data_id]
