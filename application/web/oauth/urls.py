from django.conf.urls import url

from web.oauth import views as v

urlpatterns = [
    url(r'callback/(?P<auth_type>\w+)/$', v.callback, name='auth_callback'),
    url(r'(?P<auth_type>\w+)/$', v.login, name='auth_login'),
]
