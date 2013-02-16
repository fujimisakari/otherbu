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

    url(r'^bookmark_move/$', 'bookmark_move_index', name='bookmark_move_index'),
    url(r'^bookmark_move/search/$', 'bookmark_move_search', name='bookmark_move_search'),
    url(r'^bookmark_move/exec/$', 'bookmark_move_exec', name='bookmark_move_exec'),

    url(r'^category/$', 'category_index', name='category_index'),
    url(r'^category/regist/$', 'category_regist', name='category_regist'),
    url(r'^category/edit/$', 'category_edit', name='category_edit'),
    url(r'^category/delete/$', 'category_delete', name='category_delete'),

    url(r'^page/$', 'page_index', name='page_index'),
    url(r'^page/select/(?P<page_id>\d+)/$', 'page_select', name='page_select'),
    url(r'^page/regist/$', 'page_regist', name='page_regist'),
    url(r'^page/search/$', 'page_search', name='page_search'),
    url(r'^page/edit/$', 'page_edit', name='page_edit'),
    url(r'^page/delete/$', 'page_delete', name='page_delete'),

    url(r'^design/$', 'design_index', name='design_index'),
    url(r'^design/edit/$', 'design_edit', name='design_edit'),
)
