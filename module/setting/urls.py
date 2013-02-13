# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'module.setting.views',
    url(r'^bookmark/$', 'bookmark_index', name='setting_index'),
)

urlpatterns += patterns(
    'module.setting.views',
    url(r'^bookmark/$', 'bookmark_index', name='bookmark_index'),
    url(r'^bookmark/search/$', 'bookmark_search', name='bookmark_search'),
    url(r'^bookmark/regist/$', 'bookmark_regist', name='bookmark_regist'),
    url(r'^bookmark/edit/$', 'bookmark_edit', name='bookmark_edit'),
    url(r'^bookmark/delete/$', 'bookmark_delete', name='bookmark_delete'),

    url(r'^category/$', 'category_index', name='category_index'),
    url(r'^category/regist/$', 'category_regist', name='category_regist'),
    url(r'^category/edit/$', 'category_edit', name='category_edit'),
    url(r'^category/delete/$', 'category_delete', name='category_delete'),

    url(r'^design/$', 'design_index', name='design_index'),
    url(r'^design/edit/$', 'design_edit', name='design_edit'),
)
