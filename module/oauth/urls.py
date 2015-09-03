# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'module.oauth.views',
    url(r'callback/(?P<auth_type>\w+)/$', 'callback', name='auth_callback'),
    url(r'(?P<auth_type>\w+)/$', 'login', name='auth_login'),
)
