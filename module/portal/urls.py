# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'module.portal.views',
    url(r'^$', 'index', name='portal_index'),
)
