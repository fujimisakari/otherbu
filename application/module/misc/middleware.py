import re
import traceback

from django.conf import settings
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin

from module.misc.models import ExceptionTraceback


class TemplateFilterMiddleware(MiddlewareMixin):
    """
    PCユーザー, SmartPhoneユーザーのテンプレート判定
    """
    def process_request(self, request):
        MOBILE_REGEXP = re.compile(r'Android|webOS|iPhone|iPad|iPod|BlackBerry|Windows Phone|IEMobile|Opera Mini|WILLCOM')
        if MOBILE_REGEXP.search(request.META['HTTP_USER_AGENT']) is not None:
            # SmartPhoneの場合
            request.is_smartphone = True
            settings.TEMPLATES[0]['DIRS'] = settings.SMARTPHONE_TEMPLATE_DIRS
        else:
            # PCの場合
            request.is_pc = True
            settings.TEMPLATES[0]['DIRS'] = settings.PC_TEMPLATE_DIRS


class ExceptionMiddleware(MiddlewareMixin):

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
            view_name = '(Can\'t resolve) path=' + path

        ExceptionTraceback.objects.create(
            user_id=user_id,
            view_name=view_name,
            request_path=path + '?' + request.GET.urlencode(),
            exception_type=ex.__class__.__name__,
            exception_message='ex.message',
            traceback_log=traceback_str,
            post_data=request.POST,
        )
