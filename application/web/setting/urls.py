# -*- coding: utf-8 -*-

from django.conf.urls import url
from web.setting import views as v

urlpatterns = [
    url(r'^bookmark/$', v.bookmark_index, name='bookmark_index'),
    url(r'^bookmark/search/$', v.bookmark_search, name='bookmark_search'),
    url(r'^bookmark/regist/$', v.bookmark_regist, name='bookmark_regist'),
    url(r'^bookmark/edit/$', v.bookmark_edit, name='bookmark_edit'),
    url(r'^bookmark/delete/$', v.bookmark_delete, name='bookmark_delete'),

    url(r'^bookmark_move/$', v.bookmark_move_index, name='bookmark_move_index'),
    url(r'^bookmark_move/search/$', v.bookmark_move_search, name='bookmark_move_search'),
    url(r'^bookmark_move/exec/$', v.bookmark_move_exec, name='bookmark_move_exec'),

    url(r'^category/$', v.category_index, name='category_index'),
    url(r'^category/regist/$', v.category_regist, name='category_regist'),
    url(r'^category/edit/$', v.category_edit, name='category_edit'),
    url(r'^category/delete/$', v.category_delete, name='category_delete'),

    url(r'^page/$', v.page_index, name='page_index'),
    url(r'^page/select/(?P<page_id>\d+)/$', v.page_select, name='page_select'),
    url(r'^page/regist/$', v.page_regist, name='page_regist'),
    url(r'^page/search/$', v.page_search, name='page_search'),
    url(r'^page/edit/$', v.page_edit, name='page_edit'),
    url(r'^page/delete/$', v.page_delete, name='page_delete'),

    url(r'^design/$', v.design_index, name='design_index'),
    url(r'^design/edit/$', v.design_edit, name='design_edit'),

    url(r'^import/$', v.import_index, name='import_index'),
    url(r'^import/exec/$', v.import_exec, name='import_exec'),

    url(r'^export/$', v.export_index, name='export_index'),
    url(r'^export/exec/$', v.export_exec, name='export_exec'),

    url(r'^info/$', v.info_index, name='info_index'),
]
