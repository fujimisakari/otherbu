from django.conf.urls import url

from web.help import views as v

urlpatterns = [
    url(r'^client/$', v.client_index, name='client_help_index'),
]
