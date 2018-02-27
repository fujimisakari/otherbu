from django.conf.urls import url

from web.client_api import views as v

urlpatterns = [
    url(r'^login/$', v.client_login, name='client_login'),
    url(r'^sync/$', v.sync, name='sync'),
]
