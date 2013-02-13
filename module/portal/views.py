# -*- coding: utf-8 -*-

from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from module.oauth.decorator import require_user


@require_user
def index(request):
    context = RequestContext(request, {
        'title': settings.PORTAL_TITLE,
        'current_url': reverse('portal_index'),
        'body_padding': settings.PORTAL_BODY_PADDING,  # <body>のpadding-topを定義
    })
    return render_to_response('portal/index.html', context)
