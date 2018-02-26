from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse

from module.oauth.decorator import require_user


@require_user
def index(request):
    user = request.user
    context = {
        'title': settings.PORTAL_TITLE,
        'current_url': reverse('portal_index'),
        'body_padding': settings.PORTAL_BODY_PADDING,  # <body>のpadding-topを定義
    }
    response = HttpResponse(render_to_string('portal/index.html', context, request))
    response.set_cookie('passport', value=user.passport.passport, expires=user.passport.expire_date)
    return response
