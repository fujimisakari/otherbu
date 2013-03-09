# -*- coding: utf-8 -*-

import datetime
from django.db import models
from django.conf import settings
from module.setting.models import Category, Bookmark, Design, Page


class User(models.Model):
    type = models.CharField(u'認証先', max_length=50)
    type_id = models.CharField(u'認証先ID', max_length=255)
    name = models.CharField(u'ユーザー名', max_length=50)
    user_dir = models.CharField(u'ユーザーディレクトリ名', max_length=20)
    access_token_key = models.CharField(u'アクセストークン(key)', max_length=200)
    access_token_secret = models.CharField(u'アクセストークン(secret)', max_length=200)
    page_id = models.IntegerField(u'現在のページ', default=0)
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)

    class Meta:
        unique_together = (('type', 'type_id'),)

    @property
    def category_list(self):
        c_list = Category.get_cache_user(self.pk)
        if self.page_id:
            c_list = [c for c in c_list if c.id in self.page.category_ids]
        c_list = sorted(c_list, key=lambda x: x.angle)
        c_list = sorted(c_list, key=lambda x: x.sort)
        return c_list

    @property
    def all_category_list(self):
        c_list = Category.get_cache_user(self.pk)
        c_list = sorted(c_list, key=lambda x: x.angle)
        c_list = sorted(c_list, key=lambda x: x.sort)
        return c_list

    @property
    def bookmark_list(self):
        bk_list = Bookmark.get_cache_user(self.pk)
        bk_list = sorted(bk_list, key=lambda x: x.category)
        bk_list = sorted(bk_list, key=lambda x: x.sort)
        return bk_list

    @property
    def page_list(self):
        page_list = Page.get_cache_user(self.pk)
        page_list = [page for page in page_list]
        return page_list

    @property
    def page(self):
        return Page.get_cache(self.page_id)

    @property
    def design(self):
        return Design.objects.get(user_id=self.pk)

    @property
    def passport(self):
        return Passport.objects.get(user_id=self.pk)


class Passport(models.Model):
    user_id = models.IntegerField(u'ユーザーID', db_index=True)
    passport = models.CharField(u'パスポートハッシュ', max_length=50, db_index=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)

    class Meta:
        unique_together = (('user_id', 'passport'),)

    @property
    def user(self):
        return User.objects.get(id=self.user_id)

    @property
    def expire_date(self):
        expire = datetime.timedelta(days=settings.PASSPORT_EXPIRE)
        return self.updated_at + expire
