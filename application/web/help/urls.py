# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'web.help.views',
    url(r'^client/$', 'client_index', name='client_help_index'),
)
