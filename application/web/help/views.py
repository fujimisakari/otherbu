from django.conf import settings
from django.shortcuts import render

from .context import help_context


def client_index(request):
    params = {
        'title': settings.ROOT_TITLE,
        'body_padding': settings.PORTAL_BODY_PADDING,
        'help_list': help_context,
    }
    return render(request, 'client/help_index.html', params)
