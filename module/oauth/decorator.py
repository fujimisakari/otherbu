# -*- coding: utf-8 -*-

import datetime
from functools import wraps
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from module.oauth.models import User, Passport


def _passport_check(request):
    # 開発用
    if settings.AUTO_LOGIN:
        passport_key = request.COOKIES.get('passport', None)
        request.user = User.objects.get(id=1)
        return True

    # デモページ用
    if request.session.get('DEMO_PAGE', False):
        passport_key = request.COOKIES.get('passport', None)
        request.user = User.objects.get(id=settings.DEMO_USER_ID)
        return True

    passport_key = request.COOKIES.get('passport', None)
    if passport_key:
        try:
            passport = Passport.objects.get(passport=passport_key)
        except:
            return False
        now_date = datetime.datetime.now()
        if passport.expire_date > now_date:
            request.user = passport.user
            request.session['user'] = passport.user
            return True
        else:
            return False
    else:
        return False


def require_user(view_func):
    def _wrapped_view(request, *args, **kwargs):
        has_passport = _passport_check(request)
        if has_passport or request.session.get('user', False):
            if not has_passport and request.session.get('user', False):
                user = request.session['user']
                request.user = user
            return view_func(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('root_index'))
    return wraps(view_func)(_wrapped_view)
