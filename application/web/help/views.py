# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from .context import help_context


def client_index(request):
    params = {
        'title': settings.ROOT_TITLE,
        'body_padding': settings.PORTAL_BODY_PADDING,
        'help_list': help_context,
    }
    return render_to_response('client/help_index.html', context_instance=RequestContext(request, params))
