import requests

from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

from module.oauth.handler.base import OauthBase


class OauthFacebookHandler(OauthBase):

    def auth_login(self, request):
        # 認証URLへリダイレクト
        auth_uri = 'https://www.facebook.com/v2.8/dialog/oauth'
        auth_url = '{}?client_id={}&redirect_uri={}'.format(auth_uri, settings.FACEBOOK_APP_KEY, settings.FACEBOOK_REDIRECT_URI)
        return auth_url

    def auth_callback(self, request):
        oauth_code = request.GET['code']
        token_args = {
            'client_id': settings.FACEBOOK_APP_KEY,
            'client_secret': settings.FACEBOOK_APP_SECRET,
            'code': oauth_code,
            'redirect_uri': settings.FACEBOOK_REDIRECT_URI,
        }
        # アクセストークンの取得
        res_token = requests.get('https://graph.facebook.com/v2.8/oauth/access_token', params=token_args).json()
        access_token = res_token['access_token']
        # ユーザー情報の取得
        me_args = {'access_token': access_token}
        res_me = requests.get('https://graph.facebook.com/me', params=me_args).json()
        me = Me(res_me, access_token)
        user = self.save_user(request, me, 'facebook')
        response = HttpResponseRedirect(reverse('portal_index'))
        response = self.passport_write(response, user)
        return response


class Me(object):

    def __init__(self, fb_user, access_token):
        self.id = fb_user['id']
        self.screen_name = fb_user['name']
        self.access_token_key = access_token
        self.access_token_secret = ''
        self.user_dir = fb_user['id']
