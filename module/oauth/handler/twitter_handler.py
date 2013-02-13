# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from tweepy import OAuthHandler, API
from module.oauth.handler.base import OauthBase


class OauthTwitterHandler(OauthBase):

    def get_oauth_handler(self):
        """
        TweepyのOAuthハンドラを取得
        """
        return OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)

    def get_api(self, access_token):
        """
        TweepyのAPIを取得
        """
        handler = self.get_oauth_handler()
        handler.set_access_token(access_token.key, access_token.secret)
        api = API(handler)
        return api

    def auth_login(self, request):
        handler = self.get_oauth_handler()
        # 認証URLの取得
        auth_url = handler.get_authorization_url()
        # リクエストトークンをセッションに保持
        self.set_request_token(request, handler.request_token.key, handler.request_token.secret)
        # 認証URLへリダイレクト
        return auth_url

    def auth_callback(self, request):
        oauth_token = request.GET['oauth_token']
        oauth_verifier = request.GET['oauth_verifier']
        handler = self.get_oauth_handler()
        handler.set_request_token(oauth_token, oauth_verifier)
        # アクセストークンを取得
        access_token = handler.get_access_token(oauth_verifier)
        # アクセストークンをセッションに保持
        self.set_access_token(request, access_token)
        # APIインスタンスを取得
        api = self.get_api(access_token)
        me = api.me()
        user = self.save_user(request, me, 'twitter')
        response = HttpResponseRedirect(reverse('portal_index'))
        response = self.passport_write(response, user)
        return response
