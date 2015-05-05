# -*- coding: utf-8 -*-

import urllib
import urllib2
import simplejson
# Find a query string parser
try:
    from urlparse import parse_qs
except ImportError:
    from cgi import parse_qs
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from module.oauth.handler.base import OauthBase


class OauthFacebookHandler(OauthBase):

    def auth_login(self, request):
        # 認証URLへリダイレクト
        auth_url = "https://graph.facebook.com/oauth/authorize"
        auth_url = "%s?client_id=%s&redirect_uri=%s&scope=offline_access" % (auth_url,
                                                                             settings.FACEBOOK_APP_KEY,
                                                                             settings.FACEBOOK_REDIRECT_URI)
        return auth_url

    def auth_callback(self, request):
        oauth_code = request.GET['code']
        args = {
            "client_id": settings.FACEBOOK_APP_KEY,
            "client_secret": settings.FACEBOOK_APP_SECRET,
            "code": oauth_code,
            "redirect_uri": settings.FACEBOOK_REDIRECT_URI,
        }
        # アクセストークンの取得
        response_token = urllib2.urlopen("https://graph.facebook.com/oauth/access_token?" + urllib.urlencode(args))
        query_str = parse_qs(response_token.read())
        access_token = query_str["access_token"][0]
        # ユーザー情報の取得
        args = {'access_token': access_token }
        response_me = urllib2.urlopen('https://graph.facebook.com/me?' + urllib.urlencode(args))
        json_user = response_me.read()
        me = Me(json_user, access_token)
        user = self.save_user(request, me, 'facebook')
        response = HttpResponseRedirect(reverse('portal_index'))
        response = self.passport_write(response, user)
        return response


class Me(object):
    def __init__(self, json_user, access_token):
        self.id = simplejson.loads(json_user)['id']
        self.screen_name = simplejson.loads(json_user)['name']
        self.access_token_key = access_token
        self.access_token_secret = ""
        self.user_dir = simplejson.loads(json_user)['id']
