# -*- coding: utf-8 -*-

from django.conf import settings
from module.setting.models import CategoryColor
from module.oauth.models import User


def common_context(request):
    '''
    ポータル画面、setting画面で共通で呼び出すコンテキスト
    '''
    return {
        'COLUMN': settings.COLUMN,
        'SITE_TITLE': settings.SITE_TITLE,
        'MEDIA_CSS': settings.MEDIA_CSS,
        'MEDIA_JS': settings.MEDIA_JS,
        'MEDIA_IMG': settings.MEDIA_IMG,
        'MEDIA_USER_BK_IMG': settings.MEDIA_USER_BK_IMG,
        'BK_IMAGE_NAME': settings.BK_IMAGE_NAME,
        'USER_IMAGE': settings.USER_IMAGE,
    }


def user_context(request):
    '''
    ユーザー情報を取得
    '''
    if hasattr(request, 'user'):
        user = request.user
        if isinstance(user, User):
            cc_list = CategoryColor.get_cache_all()
            cc_list = sorted(cc_list, key=lambda x: x.sort)
            return {
                'user': user,
                'category_list': user.category_list,
                'all_category_list': user.all_category_list,
                'bookmark_list': user.bookmark_list,
                'page_list': user.page_list,
                'color_list': cc_list,
                'design': user.design,
            }
        else:
            return {}
    else:
        return {}
