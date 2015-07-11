# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'module.client_api.views',
    url(r'^sync/$', 'sync', name='sync'),
)
