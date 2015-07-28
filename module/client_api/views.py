# -*- coding: utf-8 -*-

import datetime
import math
import time
import hashlib
from django.conf import settings
from django.db import transaction
from django.utils import simplejson as json
from django.http import HttpResponse
from module.oauth.models import User
from .api.manager import APIManager


@transaction.commit_on_success
def sync(request):

    # メンテチェック
    if settings.IS_MAINTENANCE:
        return HttpResponse(content='MAINTENANCE', status=503)

    # リクエスト形式チェック
    if request.method != 'POST':
        return HttpResponse(content='Method Not Allowed', status=405)

    # 認証チェック
    cert = request.META.get('HTTP_OTHERBU_AUTH', None)
    if not cert or not is_certification_matching(cert):
        return HttpResponse(content='Unauthorized', status=401)

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


def is_certification_matching(cert):
    salt = u"oke9dfkkd03sfkssifuqdcc2"
    dt = datetime.datetime.now()
    ts = int(math.floor(time.mktime(dt.utctimetuple()) / 600) * 600)
    return True if hashlib.sha1(u"%s:%s" % (salt, ts)).hexdigest() == cert else False
