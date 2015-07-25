# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def index(request):
    if request.session.get('CLIENT', False):
        del request.session['CLIENT']
        return HttpResponseRedirect(reverse('completion_client'))
    params = {
        'title': settings.ROOT_TITLE,
        'body_padding': settings.PORTAL_BODY_PADDING,
    }
    return render_to_response('index.html', context_instance=RequestContext(request, params))


def client_index(request):
    params = {
        'title': settings.ROOT_TITLE,
        'body_padding': settings.PORTAL_BODY_PADDING,
    }
    return render_to_response('client/index.html', context_instance=RequestContext(request, params))
