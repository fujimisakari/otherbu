# -*- coding: utf-8 -*-

import re
import traceback
from uamobile import detect
from django.core.urlresolvers import resolve
from django.conf import settings
from django.http import HttpResponse
from module.misc.models import ExceptionTraceback


class TemplateFilterMiddleware(object):
    '''
    PCユーザー,SmartPhoneユーザーのテンプレート判定
    '''
    def process_request(self, request):
        request.device = detect(request.META)
        if not request.device.is_nonmobile():
            return HttpResponse(u'<h3>対応端末ではありません</h3>')
        else:
            ua = request.device.useragent
            p = r"(iPhone|Android)"
            r = re.compile(p)
            if r.search(ua):
                # SmartPhoneの場合
                request.is_smartphone = True
                settings.TEMPLATE_DIRS = settings.SMARTPHONE_TEMPLATE_DIRS
            else:
                # PCの場合
                request.is_pc = True
                settings.TEMPLATE_DIRS = settings.PC_TEMPLATE_DIRS


class ExceptionMiddleware(object):

    def process_exception(self, request, ex):
        traceback_str = traceback.format_exc()
        user_id = request.user.id
        if not user_id:
            user_id = '-'

        path = request.path
        view_name = None
        try:
            view_name = resolve(path).view_name
        except:
            view_name = "(Can't resolve) path=" + path

        ExceptionTraceback.objects.create(
            user_id=user_id,
            view_name=view_name,
            request_path=path + '?' + request.GET.urlencode(),
            exception_type=ex.__class__.__name__,
            exception_message=unicode(ex.message),
            traceback_log=traceback_str,
            post_data=request.POST,
        )
