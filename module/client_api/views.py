# -*- coding: utf-8 -*-

from django.db import transaction

from django.utils import simplejson as json
from django.http import HttpResponse

from . import api


@transaction.commit_on_success
def sync(request):

    # todo 認証チェック

    # post以外は弾く

    request_data = json.loads(request.body)

    # 追加や更新、削除などで重複データがあれば解消させる(優先順位: 削除 > 更新 > 追加)
    delete_category_id_list = [category_id for category_id, _ in request_data['Category']['delete'].items()]
    request_data['Category'] = api.delete_duplicate_date(request_data['Category'])
    request_data['Page'] = api.delete_duplicate_date(request_data['Page'])
    request_data['Bookmark'] = api.delete_duplicate_date(request_data['Bookmark'])

    # todo あとで消す
    request_data['User'] = {
        'id': '1',
        'page_id': '16',
        'updated_at': '2015,5,6,23,26,14',
    }

    # データ追加
    response_data_dict = api.insert_date(request_data, delete_category_id_list)

    # データ更新
    update_dict = api.update_date(request_data, response_data_dict)

    # 削除対象を取得

    ret_json = {
        'user': update_dict['user'],
        'design': update_dict['design'],
        'update_page_list': response_data_dict['Page'],
        'update_category_list': response_data_dict['Category'],
        'update_bookmark_list': response_data_dict['Bookmark'],
        'delete_page_list': [],
        'delete_category_list': [],
        'delete_bookmark_list': [],
    }
    json_data = json.dumps(ret_json, ensure_ascii=False)
    print json_data

    return HttpResponse(json_data, mimetype='application/json')
