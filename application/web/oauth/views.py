import datetime
import uuid

from django.conf import settings
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse

from module.oauth.handler.facebook_handler import OauthFacebookHandler
from module.oauth.handler.twitter_handler import OauthTwitterHandler


def select_auth_type(auth_type):
    handler_map = {'twitter': OauthTwitterHandler(),
                   'facebook': OauthFacebookHandler()}
    handler = handler_map.get(auth_type)
    if handler:
        return handler
    return HttpResponseRedirect(reverse('root_index'))


def login(request, auth_type=None):
    if not auth_type:
        return HttpResponseRedirect(reverse('root_index'))

    if settings.AUTO_LOGIN:
        now = datetime.datetime.now()
        expire = datetime.timedelta(days=settings.PASSPORT_EXPIRE)
        expire_date = now + expire
        response = HttpResponseRedirect(reverse('portal_index'))
        response.set_cookie('passport', value=uuid.uuid4(), expires=expire_date)
        return response

    if request.session.get('DEMO_PAGE', False):
        del request.session['DEMO_PAGE']

    auth_handler = select_auth_type(auth_type)
    auth_url = auth_handler.auth_login(request)
    return HttpResponseRedirect(auth_url)


def demo_page(request):
    if settings.AUTO_LOGIN:
        return HttpResponseRedirect(reverse('root_index'))

    request.session['DEMO_PAGE'] = True
    now = datetime.datetime.now()
    expire = datetime.timedelta(days=settings.PASSPORT_EXPIRE)
    expire_date = now + expire
    response = HttpResponseRedirect(reverse('portal_index'))
    response.set_cookie('passport', value=uuid.uuid4(), expires=expire_date)
    return response


@transaction.atomic
def callback(request, auth_type=None):
    if not auth_type:
        return HttpResponseRedirect(reverse('root_index'))

    auth_handler = select_auth_type(auth_type)
    response = auth_handler.auth_callback(request)
    return response


def logout(request):
    # クッキーとセッションの情報を消す
    if request.session.get('user', False):
        del request.session['user']

    response = HttpResponseRedirect(reverse('root_index'))
    response.delete_cookie('passport')
    return response
