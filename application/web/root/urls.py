# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'web.root.views',
    url(r'^$', 'index', name='root_index'),
)