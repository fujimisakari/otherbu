# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'module.root.views',
    url(r'^$', 'index', name='root_index'),
    url(r'^client/$', 'client_index', name='client_root_index'),
)
