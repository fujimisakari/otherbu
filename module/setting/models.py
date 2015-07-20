# -*- coding: utf-8 -*-

from django.db import models
from module.misc.common_models import AbustractCachedModel


class Category(AbustractCachedModel):
    user_id = models.IntegerField(u'ユーザーID', db_index=True)
    mobile_id = models.CharField(u'スマホ版のID', max_length=100, blank=True, null=True)
    name = models.CharField(u'カテゴリ名', max_length=100)
    angle = models.IntegerField(u'位置', default=0)
    sort = models.IntegerField(u'Sort番号', blank=True, null=True)
    color_id = models.IntegerField(u'カテゴリカラーID', default=18)
    tag_open = models.BooleanField(u'初期開放', default=1)
    sync_flag = models.BooleanField(u'同期対象', default=1)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)
    # 複合インデックス： ['user_id', 'angle'], ['user_id', 'sync_flag']

    def __str__(self):
        member_str = '\nid={},\nuser_id={},\nmobile_id={},\nname={},\nangle={},\nsort={},\ncolor_id={},\ntag_open={},\nsync_flag={},\nupdated_at={}\n'
        return member_str.format(self.id, self.user_id, self.mobile_id, self.name, self.angle,
                                 self.sort, self.color_id, self.tag_open, self.sync_flag, self.updated_at)

    def to_dict(self):
        target = ['id', 'name', 'angle', 'sort', 'color_id', 'tag_open']
        return dict((x, getattr(self, x)) for x in target)

    def update_sync(self, sync_data):
        self.mobile_id = sync_data['id']
        self.name = sync_data['name']
        self.angle = int(sync_data['angle'])
        self.sort = int(sync_data['sort'])
        self.color_id = int(sync_data['color_id'])
        self.tag_open = int(sync_data['tag_open'])
        self.sync_flag = False
        self.save()

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
    mobile_id = models.CharField(u'スマホ版のID', max_length=100, blank=True, null=True)
    name = models.CharField(u'カテゴリ名', max_length=100)
    category_ids_str = models.TextField(u'ページに含むカテゴリ')
    angle_ids_str = models.TextField(u'ページに含むカテゴリ位置', blank=True, null=True)
    sort_ids_str = models.TextField(u'ページに含むカテゴリ順番', blank=True, null=True)
    sync_flag = models.BooleanField(u'同期対象', default=1)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)
    # 複合インデックス： ['user_id', 'angle'], ['user_id', 'sync_flag']

    def __str__(self):
        member_str = '\nid={}\nuser_id={},\nmobile_id={},\nname={},\ncategory_ids_str={},\nangle_ids_str={},\nsort_ids_str={},\nsync_flag={},\nupdated_at={}\n'
        return member_str.format(self.id, self.user_id, self.mobile_id, self.name, self.category_ids_str,
                                 self.angle_ids_str, self.sort_ids_str, self.sync_flag, self.updated_at)

    def to_dict(self):
        target = ['id', 'user_id', 'mobile_id', 'name', 'category_ids_str', 'angle_ids_str', 'sort_ids_str']
        return dict((x, getattr(self, x)) for x in target)

    def update_sync(self, sync_data):
        self.mobile_id = sync_data['id']
        self.name = sync_data['name']
        self.category_ids_str = sync_data['category_ids_str']
        self.angle_ids_str = sync_data['angle_ids_str']
        self.sort_ids_str = sync_data['sort_ids_str']
        self.sync_flag = False
        self.save()

    @property
    def category_ids(self):
        category_ids = self.category_ids_str.split(',')
        category_ids = [int(c) for c in category_ids]
        return category_ids

    @property
    def angle_dict(self):
        result_dict = {}
        if self.angle_ids_str:
            angle_ids = self.angle_ids_str.split(',')
            for angle_id_str in angle_ids:
                angle_list = angle_id_str.split(':')
                category_id = int(angle_list[0])
                angle_id = int(angle_list[1])
                result_dict[category_id] = angle_id
        return result_dict

    @property
    def sort_dict(self):
        result_dict = {}
        if self.sort_ids_str:
            sort_ids = self.sort_ids_str.split(',')
            for sort_id_str in sort_ids:
                sort_list = sort_id_str.split(':')
                category_id = int(sort_list[0])
                sort_id = int(sort_list[1])
                result_dict[category_id] = sort_id
        return result_dict


class Bookmark(AbustractCachedModel):
    user_id = models.IntegerField(u'ユーザーID', db_index=True)
    mobile_id = models.CharField(u'スマホ版のID', max_length=100, blank=True, null=True)
    category_id = models.IntegerField(u'カテゴリID')
    name = models.CharField(u'Bookmark名', max_length=200, default=0)
    url = models.CharField(u'URL', max_length=200)
    sort = models.IntegerField(u'Sort番号', blank=True, null=True)
    sync_flag = models.BooleanField(u'同期対象', default=1)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)
    # 複合インデックス： ['user_id', 'category_id'], ['user_id', 'sync_flag']

    def __str__(self):
        member_str = '\nid={},\nuser_id={},\nmobile_id={},\ncategory_id={},\nname={},\nurl={},\nsort={},\nsync_flag={},\nupdated_at={}\n'
        return member_str.format(self.id, self.user_id, self.mobile_id, self.category_id,
                                 self.name, self.url, self.sort, self.sync_flag, self.updated_at)

    @property
    def category(self):
        return Category.get_cache(self.category_id)

    def to_dict(self):
        target = ['id', 'category_id', 'name', 'url', 'sort']
        return dict((x, getattr(self, x)) for x in target)

    def update_sync(self, sync_data, category_id):
        self.mobile_id = sync_data['id']
        self.name = sync_data['name']
        self.category_id = category_id
        self.url = sync_data['url']
        self.sort = int(sync_data['sort'])
        self.sync_flag = False
        self.save()


class Design(AbustractCachedModel):
    user_id = models.IntegerField(u'ユーザーID', unique=True)
    linkmark_flg = models.BooleanField(u'リンクマーク', default=0)
    link_color = models.CharField(u'リンク色', max_length=10, default='#005580')
    category_back_color = models.CharField(u'カテゴリ背景色', max_length=10, default='#FFF')
    portal_back_kind = models.BooleanField(u'画面背景設定', default=0)
    portal_back_color = models.CharField(u'画面背景色', max_length=10, default='#FFF')
    image_position = models.CharField(u'画像の配置', max_length=30)
    bk_image_ext = models.CharField(u'背景画像の拡張子', max_length=30, null=True)
    sync_flag = models.BooleanField(u'同期対象', default=1)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)

    def __str__(self):
        member_str = '\nid={},\nlinkmark_flg={},\nlink_color={},\ncategory_back_color={},\nportal_back_kind={},\nportal_back_color={},\nimage_position={},\nbk_image_ext={},\nsync_flag={},\nupdated_at={}\n'
        return member_str.format(self.id, self.linkmark_flg, self.link_color, self.category_back_color, self.portal_back_kind,
                                 self.portal_back_color, self.image_position, self.bk_image_ext, self.sync_flag, self.updated_at)

    def to_dict(self):
        target = ['id', 'category_back_color', 'link_color']
        return dict((x, getattr(self, x)) for x in target)


class DeleteManager(AbustractCachedModel):
    """
    同期するために削除したIDを保持するクラス
    """
    user_id = models.IntegerField(u'ユーザーID', unique=True)
    bookmark = models.TextField(u'ブックマークの削除ID', blank=True, null=True)
    category = models.TextField(u'カテゴリの削除ID', blank=True, null=True)
    page = models.TextField(u'ページの削除ID', blank=True, null=True)

    def __str__(self):
        member_str = '\nid={},\nuser_id={},\nbookmark={},\ncategory={},\npage={}\n'
        return member_str.format(self.id, self.user_id, self.bookmark, self.category, self.page)

    @property
    def user(self):
        from module.oauth.models import User
        return User.objects.get(id=self.user_id)

    def add_delete_id(self, data_type, delete_id):
        if self.user.use_mobile and hasattr(self, data_type):
            if getattr(self, data_type):
                id_list = getattr(self, data_type).split(u',')
                id_list.append(delete_id)
                setattr(self, data_type, u','.join(id_list))
            else:
                setattr(self, data_type, str(delete_id))
            self.save()

    def reset(self):
        self.bookmark = ''
        self.category = ''
        self.page = ''
        self.save()
