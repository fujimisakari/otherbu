import abc
import datetime


class BaseController(abc.ABC):

    @abc.abstractmethod
    def init_setup(self, **kw):
        """
        初期設定
        """
        pass

    @abc.abstractmethod
    def run(self):
        """
        実行
        """
        pass

    @abc.abstractmethod
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

    def _update_category_id_by_page_data(self, page_data, category_map, delete_category_id_list):
        """
        pageにClientで作成されたIDを保持してる場合は,DBで生成されたIDに差し替える
        """
        # 削除されたCategory情報を保持しないようにする
        def _deta_format(id_str):
            str_list = []
            ids = [x for x in id_str.split(',') if x]
            for _id_str in ids:
                alist = _id_str.split(':')
                category_id = alist[0]
                value = alist[1]
                if category_id not in delete_category_id_list:
                    str_list.append('{}:{}'.format(category_id, value))
            return str_list

        for mobile_id, category in category_map.items():
            page_data['category_ids_str'] = page_data['category_ids_str'].replace(str(mobile_id), str(category['id']))
            page_data['angle_ids_str'] = page_data['angle_ids_str'].replace(str(mobile_id), str(category['id']))
            page_data['sort_ids_str'] = page_data['sort_ids_str'].replace(str(mobile_id), str(category['id']))

        # カテゴリ
        category_id_list = page_data['category_ids_str'].split(',')
        category_ids = []
        for category_id in category_id_list:
            if category_id not in delete_category_id_list:
                category_ids.append(str(category_id))
        page_data['category_ids_str'] = ','.join(category_ids)
        # アングル
        page_data['angle_ids_str'] = ','.join(_deta_format(page_data['angle_ids_str']))
        # 順番
        page_data['sort_ids_str'] = ','.join(_deta_format(page_data['sort_ids_str']))
