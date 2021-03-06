from django.conf.urls import include, url

from web.ajax.views import (
    get_page_title,
    get_sugetst,
    swap_category,
    tag_open,
    update_color
)
from web.oauth.views import demo_page, logout

urlpatterns = [
    url(r'^$', include('web.portal.urls')),
    url(r'^$', include('web.ajax.urls')),
    url(r'^login/', include('web.root.urls')),
    url(r'^oauth/', include('web.oauth.urls')),
    url(r'^setting/', include('web.setting.urls')),
    url(r'^client_api/', include('web.client_api.urls')),
    url(r'^help/', include('web.help.urls')),
    url(r'^demo_page/$', demo_page, name='demo_page'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^get_title/$', get_page_title, name='get_title'),
    url(r'^get_suggest/$', get_sugetst, name='get_suggest'),
    url(r'^swap_category/$', swap_category, name='swap_category'),
    url(r'^tag_open/$', tag_open, name='swap_category'),
    url(r'^update_color/$', update_color, name='update_color'),
]
