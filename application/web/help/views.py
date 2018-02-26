from django.conf import settings
from django.shortcuts import render_to_response

from .context import help_context


def client_index(request):
    params = {
        'title': settings.ROOT_TITLE,
        'body_padding': settings.PORTAL_BODY_PADDING,
        'help_list': help_context,
    }
    return render_to_response(request, 'client/help_index.html', params)
