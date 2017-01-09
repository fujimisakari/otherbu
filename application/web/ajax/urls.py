# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'web.ajax.views',
    url(r'^get_title/$', 'get_page_title', name='get_title'),
    url(r'^get_suggest/$', 'get_sugetst', name='get_suggest'),
    url(r'^swap_category/$', 'swap_category', name='swap_category'),
    url(r'^tag_open/$', 'tag_open', name='swap_category'),
    url(r'^update_color/$', 'update_color', name='update_color'),
)
