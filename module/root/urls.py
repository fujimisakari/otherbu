# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'module.root.views',
    url(r'^$', 'index', name='root_index'),
)
