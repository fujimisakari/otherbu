# -*- coding: utf-8 -*-

import datetime
import urllib
import math
import time
import hashlib
from django.conf import settings
from django.db import transaction
from django.utils import simplejson as json
from django.http import HttpResponse
from module.oauth.models import User
from module.oauth.handler.base import OauthBase
from .api.manager import APIManager


@transaction.commit_on_success
def client_login(request):

    # 認証チェック
    http_response = check_certification(request)
    if http_response:
        return http_response

    request_data = json.loads(request.body)
    name = request_data['name']
    type_id = request_data['type_id']
    type_name = request_data['auth_type']

    user, is_new = User.objects.get_or_create(type=type_name, type_id=type_id)

    if is_new:
        # 初めてのユーザーには初期設定を当てる
        user.name = name
        user.user_dir = type_id
        OauthBase().init_setup(user, type_id, type_name)
        user.save()

    # ユーザー画像を取得
    if type_name == "twitter":
        image_url = request_data['profile_image_url']
    elif type_name == "facebook":
        image_url = "https://graph.facebook.com/%s/picture" % (type_id)
    user_path = "%s/%s/%s/%s" % (settings.USER_IMG_DIR, type_name, type_id, settings.USER_IMAGE)
    urllib.urlretrieve(image_url, user_path)

    ret_json = {'user_data': user.to_dict()}
    json_data = json.dumps(ret_json, ensure_ascii=False)
    return HttpResponse(json_data, mimetype='application/json')


@transaction.commit_on_success
def sync(request):

    # 認証チェック
    http_response = check_certification(request)
    if http_response:
        return http_response

    request_data = json.loads(request.body)

    # ユーザーチェック
    if int(request_data['User']['id']) == 0:
        return HttpResponse(content='Forbidden', status=403)

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


def check_certification(request):
    # メンテチェック
    if settings.IS_MAINTENANCE:
        return HttpResponse(content='MAINTENANCE', status=503)

    # リクエスト形式チェック
    if request.method != 'POST':
        return HttpResponse(content='Method Not Allowed', status=405)

    # 認証チェック
    # cert = request.META.get('HTTP_OTHERBU_AUTH', None)
    # if not cert or not is_certification_matching(cert):
    #     return HttpResponse(content='Unauthorized', status=401)

    return None


def is_certification_matching(received_cert):
    salt = u"oke9dfkkd03sfkssifuqdcc2"
    dt = datetime.datetime.now()
    ts = int(math.floor(time.mktime(dt.utctimetuple()) / 600) * 600)
    current_cert = hashlib.sha1(u"%s:%s" % (salt, ts)).hexdigest()

    minutes_list = [0, -30, -20, -10, 10, 20, 30]
    for minutes in minutes_list:
        if received_cert == current_cert:
            return True
    return False
