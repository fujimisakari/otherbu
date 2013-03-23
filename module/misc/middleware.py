# -*- coding: utf-8 -*-

import re
from uamobile import detect
from django.conf import settings
from django.http import HttpResponse


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
