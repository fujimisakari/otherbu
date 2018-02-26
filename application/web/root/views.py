from django.conf import settings
from django.shortcuts import render


def index(request):
    if request.session.get('DEMO_PAGE', False):
        del request.session['DEMO_PAGE']
    params = {
        'title': settings.ROOT_TITLE,
        'body_padding': settings.PORTAL_BODY_PADDING,
    }
    return render(request, 'index.html', params)
