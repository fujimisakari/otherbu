# -*- coding: utf-8 -*-

import datetime
from functools import wraps
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from module.oauth.models import User, Passport


def _passport_check(request):
    if settings.AUTO_LOGIN:
        passport_key = request.COOKIES.get('passport', None)
        if passport_key:
            request.user = User.objects.get(id=1)
            return True
        else:
            return False

    passport_key = request.COOKIES.get('passport', None)
    if passport_key:
        try:
            passport = Passport.objects.get(passport=passport_key)
        except:
            return False
        now_date = datetime.datetime.now()
        if passport.expire_date > now_date:
            request.user = passport.user
        return True
    else:
        return False


def require_user(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if _passport_check(request):
            return view_func(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('root_index'))
    return wraps(view_func)(_wrapped_view)
