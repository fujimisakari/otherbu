# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'web.client_api.views',
    url(r'^login/$', 'client_login', name='client_login'),
    url(r'^sync/$', 'sync', name='sync'),
)
