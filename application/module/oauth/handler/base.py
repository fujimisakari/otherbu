import uuid

import requests
from django.conf import settings

from module.misc.common_api import s3_object_copy, s3_uploader
from module.oauth.models import Passport, User
from module.setting.models import Bookmark, Category, DeleteManager, Design


class OauthBase(object):

    def get_access_token(self, request):
        return request.session['access_token']

    def set_access_token(self, request, access_token):
        request.session['access_token'] = access_token

    def get_request_token(self, request, key):
        return request.session[key]

    def set_request_token(self, request, key, token):
        request.session[key] = token

    def passport_write(self, response, user):
        passport, _ = Passport.objects.get_or_create(user_id=user.pk)
        passport.passport = uuid.uuid4()
        passport.save()
        response.set_cookie('passport', value=passport.passport, expires=passport.expire_date)
        return response

    def save_user(self, request, me, auth_type):
        user, is_new = User.objects.get_or_create(type=auth_type, type_id=me.id)
        user.name = me.screen_name
        if auth_type == 'twitter':
            user_dir = me.id
            access_token = self.get_access_token(request)
            user.access_token_key = access_token[0]
            user.access_token_secret = access_token[1]
            image_url = me.profile_image_url
        elif auth_type == 'facebook':
            user_dir = me.id
            user.access_token_key = me.access_token_key
            user.access_token_secret = me.access_token_secret
            image_url = 'https://graph.facebook.com/{}/picture'.format(user_dir)
        user.user_dir = user_dir
        if is_new:
            # 初めてのユーザーには初期設定を当てる
            self.init_setup(user, user_dir, auth_type)
        user.save()
        # ユーザー画像を取得
        res = requests.get(image_url)
        user_path = '{}/{}/{}/{}'.format(settings.USER_IMG_DIR, auth_type, user_dir, settings.USER_IMAGE)
        s3_uploader(user_path, res.content, 'jpg')
        return user

    def init_setup(self, user, user_dir, auth_type, need_sample_data=True):
        # サンプル背景を配置
        sample_img_path = '{}/{}/{}/{}.jpg'.format(settings.USER_IMG_DIR, auth_type, user_dir, settings.BK_IMAGE_NAME)
        s3_object_copy(settings.SAMPLE_IMG_PATH, sample_img_path)

        # デザインの初期設定
        Design.objects.create(
            user_id=user.id,
            linkmark_flg=settings.LINKMARK_FLG,
            link_color=settings.LINK_COLOR,
            category_back_color=settings.CATEGORY_BACK_COLOR,
            portal_back_kind=settings.PORTAL_BACK_KIND,
            portal_back_color=settings.PORTAL_BACK_COLOR,
            image_position=settings.IMAGE_POSITION,
            bk_image_ext=settings.BK_IMAGE_EXT,
        )

        # 削除の同期管理クラスのインスタンスを生成
        DeleteManager.objects.create(user_id=user.id)

        # カテゴリ, ブックマークの初期設定
        if need_sample_data:
            bookmark_list = []
            for init_data in settings.INIT_DATA_LIST:

                category = Category(
                    user_id=user.id,
                    name=init_data['category'][0],
                    angle=init_data['category'][1],
                    sort=init_data['category'][2],
                    color_id=init_data['category'][3],
                    tag_open=init_data['category'][4],
                )
                category.save()

                for b_tupl in init_data['bookmark']:
                    bookmark = Bookmark(
                        user_id=user.id,
                        category_id=category.id,
                        name=b_tupl[0],
                        url=b_tupl[1],
                        sort=b_tupl[2],
                    )
                    bookmark_list.append(bookmark)
            Bookmark.objects.bulk_create(bookmark_list)
