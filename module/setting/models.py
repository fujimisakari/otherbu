# -*- coding: utf-8 -*-

from django.db import models
from module.misc.common_models import AbustractCachedModel


class Category(AbustractCachedModel):
    user_id = models.IntegerField(u'ユーザーID', db_index=True)
    name = models.CharField(u'カテゴリ名', max_length=100)
    angle = models.IntegerField(u'位置', default=0)
    sort = models.IntegerField(u'Sort番号', blank=True, null=True)
    color_id = models.IntegerField(u'カテゴリカラーID', default=18)
    tag_open = models.BooleanField(u'初期開放', default=1)
    # 複合インデックス： ['user_id', 'angle']

    @property
    def bookmark_list(self):
        bk_list = Bookmark.get_cache_user(self.user_id)
        bk_list = [bk for bk in bk_list if bk.category_id == self.pk]
        bk_list = sorted(bk_list, key=lambda x: x.sort)
        return bk_list

    @property
    def color(self):
        return CategoryColor.get_cache(self.color_id)


class CategoryColor(AbustractCachedModel):
    name = models.CharField(u'カラー名', max_length=30)
    thumbnail_color_code = models.CharField(u'選択サムネイル_カラーコード', max_length=10)
    color_code1 = models.CharField(u'カラーコード1', max_length=10)
    color_code2 = models.CharField(u'カラーコード2', max_length=10)
    color_code3 = models.CharField(u'カラーコード3', max_length=10)
    font_color = models.CharField(u'fontカラー', max_length=10)
    icon_color = models.CharField(u'iconカラー', max_length=10, default='white')
    sort = models.IntegerField(u'順番')


class Page(AbustractCachedModel):
    user_id = models.IntegerField(u'ユーザーID', db_index=True)
    name = models.CharField(u'カテゴリ名', max_length=100)
    category_ids_str = models.CharField(u'ページに含むカテゴリ', max_length=255)

    @property
    def category_ids(self):
        category_ids = self.category_ids_str.split(',')
        category_ids = [int(c) for c in category_ids]
        return category_ids


class Bookmark(AbustractCachedModel):
    user_id = models.IntegerField(u'ユーザーID', db_index=True)
    category_id = models.IntegerField(u'カテゴリID')
    name = models.CharField(u'Bookmark名', max_length=200, default=0)
    url = models.CharField(u'URL', max_length=200)
    sort = models.IntegerField(u'Sort番号', blank=True, null=True)
    # 複合インデックス： ['user_id', 'category_id']

    @property
    def category(self):
        return Category.get_cache(self.category_id)


class Design(models.Model):
    user_id = models.IntegerField(u'ユーザーID', unique=True, db_index=True)
    linkmark_flg = models.BooleanField(u'リンクマーク', default=0)
    link_color = models.CharField(u'リンク色', max_length=10, default='#005580')
    category_back_color = models.CharField(u'カテゴリ背景色', max_length=10, default='#FFF')
    portal_back_kind = models.BooleanField(u'画面背景設定', default=0)
    portal_back_color = models.CharField(u'画面背景色', max_length=10, default='#FFF')
    image_position = models.CharField(u'画像の配置', max_length=30)
    bk_image_ext = models.CharField(u'背景画像の拡張子', max_length=30, null=True)
