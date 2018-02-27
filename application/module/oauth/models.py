import datetime

from django.conf import settings
from django.db import models

from module.setting.models import (
    Bookmark,
    Category,
    DeleteManager,
    Design,
    Page
)


class User(models.Model):
    type = models.CharField('認証先', max_length=50)
    type_id = models.CharField('認証先ID', max_length=255)
    name = models.CharField('ユーザー名', max_length=50)
    user_dir = models.CharField(u'ユーザーディレクトリ名', max_length=20)
    access_token_key = models.CharField('アクセストークン(key)', max_length=255)
    access_token_secret = models.CharField('アクセストークン(secret)', max_length=255)
    page_id = models.IntegerField('現在のページ', default=0)
    sync_flag = models.BooleanField('同期対象', default=1)
    use_mobile = models.BooleanField('モバイル版を使用してるかどうか', default=0)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        unique_together = (('type', 'type_id'),)

    def to_dict(self):
        target = ['id', 'name', 'type', 'type_id', 'page_id']
        return dict((x, getattr(self, x)) for x in target)

    @property
    def image_dir_path(self):
        return '{}user/{}/{}'.format(settings.MEDIA_URL, self.type, self.user_dir)

    @property
    def category_list(self):
        c_list = Category.get_cache_user(self.pk)
        if self.page:
            c_list = [c for c in c_list if c.id in self.page.category_ids]
            angle_dict = self.page.angle_dict
            sort_dict = self.page.sort_dict
            for c in c_list:
                if angle_dict:
                    c.angle = angle_dict[c.id]
                if sort_dict:
                    c.sort = sort_dict[c.id]
        c_list = sorted(c_list, key=lambda x: x.angle)
        c_list = sorted(c_list, key=lambda x: x.sort)
        return c_list

    @property
    def no_cache_category_list(self):
        c_list = Category.objects.filter(user_id=self.pk)
        if self.page:
            try:
                c_list = [c for c in c_list if c.id in self.page.category_ids]
                angle_dict = self.page.angle_dict
                sort_dict = self.page.sort_dict
                for c in c_list:
                    if angle_dict:
                        c.angle = angle_dict[c.id]
                    if sort_dict:
                        c.sort = sort_dict[c.id]
            except:
                self.page_id = 0
                self.save()
        c_list = sorted(c_list, key=lambda x: x.angle)
        c_list = sorted(c_list, key=lambda x: x.sort)
        return c_list

    @property
    def all_category_list(self):
        c_list = Category.get_cache_user(self.pk)
        c_list = sorted(c_list, key=lambda x: x.name)
        return c_list

    @property
    def no_cache_all_category_list(self):
        c_list = Category.objects.filter(user_id=self.pk)
        c_list = sorted(c_list, key=lambda x: x.angle)
        c_list = sorted(c_list, key=lambda x: x.sort)
        return c_list

    @property
    def bookmark_list(self):
        bk_list = Bookmark.get_cache_user(self.pk)
        bk_list = sorted(bk_list, key=lambda x: x.category_id)
        bk_list = sorted(bk_list, key=lambda x: x.sort)
        return bk_list

    @property
    def no_cache_bookmark_list(self):
        bk_list = Bookmark.objects.filter(user_id=self.pk)
        bk_list = sorted(bk_list, key=lambda x: x.category_id)
        bk_list = sorted(bk_list, key=lambda x: x.sort)
        return bk_list

    @property
    def page_list(self):
        page_list = Page.get_cache_user(self.pk)
        return page_list

    @property
    def no_cache_page_list(self):
        page_list = Page.objects.filter(user_id=self.pk)
        return page_list

    @property
    def page(self):
        return Page.get_cache(self.page_id)

    @property
    def design(self):
        return Design.get_cache_user(self.pk)[0]

    @property
    def delete_manager(self):
        return DeleteManager.get_cache_user(self.pk)[0]

    @property
    def passport(self):
        return Passport.objects.get(user_id=self.pk)


class Passport(models.Model):
    user_id = models.IntegerField('ユーザーID', db_index=True)
    passport = models.CharField('パスポートハッシュ', max_length=50, db_index=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        unique_together = (('user_id', 'passport'),)

    @property
    def user(self):
        return User.objects.get(id=self.user_id)

    @property
    def expire_date(self):
        expire = datetime.timedelta(days=settings.PASSPORT_EXPIRE)
        return self.updated_at + expire
