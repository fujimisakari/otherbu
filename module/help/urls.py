# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'module.help.views',
    url(r'^$', 'client_index', name='client_help_index'),
)
