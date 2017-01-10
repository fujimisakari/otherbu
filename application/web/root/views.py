# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    if request.session.get('DEMO_PAGE', False):
        del request.session['DEMO_PAGE']
    params = {
        'title': settings.ROOT_TITLE,
        'body_padding': settings.PORTAL_BODY_PADDING,
    }
    return render_to_response('index.html', context_instance=RequestContext(request, params))