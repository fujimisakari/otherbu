# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from module.ajax.views import get_page_title, get_sugetst, swap_category, tag_open, update_color
from module.oauth.views import logout, demo_page

urlpatterns = patterns(
    '',
    (r'^$', include('module.portal.urls')),
    (r'^login/', include('module.root.urls')),
    (r'^oauth/', include('module.oauth.urls')),
    (r'^setting/', include('module.setting.urls')),
    url(r'^demo_page/$', demo_page, name='demo_page'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^get_title/$', get_page_title, name='get_title'),
    url(r'^get_suggest/$', get_sugetst, name='get_suggest'),
    url(r'^swap_category/$', swap_category, name='swap_category'),
    url(r'^tag_open/$', tag_open, name='swap_category'),
    url(r'^update_color/$', update_color, name='update_color'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
