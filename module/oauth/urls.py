# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'module.oauth.views',
    url(r'callback/(?P<auth_type>\w+)/$', 'callback', name='auth_callback'),
    url(r'completion/$', 'completion_client', name='completion_client'),
    url(r'(?P<auth_type>\w+)/$', 'login', name='auth_login'),
    url(r'(?P<auth_type>\w+)/client/$', 'login_client', name='auth_login_client'),
)
