from django.conf.urls import url

from web.ajax import views as v

urlpatterns = [
    url(r'^get_title/$', v.get_page_title, name='get_title'),
    url(r'^get_suggest/$', v.get_sugetst, name='get_suggest'),
    url(r'^swap_category/$', v.swap_category, name='swap_category'),
    url(r'^tag_open/$', v.tag_open, name='swap_category'),
    url(r'^update_color/$', v.update_color, name='update_color'),
]
