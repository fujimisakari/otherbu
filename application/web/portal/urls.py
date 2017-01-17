# -*- coding: utf-8 -*-

from django.conf.urls import url
from web.portal import views as v

urlpatterns = [
    url(r'^$', v.index, name='portal_index'),
]
