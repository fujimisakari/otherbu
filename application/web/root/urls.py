from django.conf.urls import url

from web.root import views as v

urlpatterns = [
    url(r'^$', v.index, name='root_index'),
]
