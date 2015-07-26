# -*- coding: utf-8 -*-

from django.db import transaction
from django.utils import simplejson as json
from django.http import HttpResponse
from module.oauth.models import User
from .api.manager import APIManager


@transaction.commit_on_success
def sync(request):

    # post以外は弾く

    # todo 認証チェック

    request_data = json.loads(request.body)

    # exception時のため、ユーザーデータをセットしておく
    user = User.objects.get(id=request_data['User']['id'])
    request.user = user

    # 同期
    manager = APIManager(user, request_data)
    manager.run_sync()

    ret_json = {'update_data': manager.update_response,
                'delete_data': manager.delete_response}
    json_data = json.dumps(ret_json, ensure_ascii=False)

    return HttpResponse(json_data, mimetype='application/json')
