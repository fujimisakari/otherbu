import os

from django.conf import settings

from module.misc.common_api import url_exchnge
from module.misc.html_parser import get_import_list
from module.setting.forms import ImportFormSet
from module.setting.models import Bookmark, Category, Page


def get_import_form():
    return ImportFormSet()


def import_proc(request, user):
    # 現在設定中のブックマーク情報の削除
    Category.objects.filter(user_id=user.id).delete()
    Page.objects.filter(user_id=user.id).delete()
    Bookmark.objects.filter(user_id=user.id).delete()
    user.page_id = 0
    user.save()

    # アップロードファイルからブックマークリストを作成
    file_name = '{}/tmp_bookmark_{}'.format(settings.USER_TMP_DIR, user.id)
    upfile = request.FILES['form-0-bookmark_upload']
    create_file = open(file_name, mode='w')
    for chunk in upfile.chunks():
        create_file.write(chunk)
    create_file.close()
    bookmark_html = open(file_name).read()
    os.remove(file_name)
    bookmark_list = get_import_list(bookmark_html)

    # カテゴリ名リストを作成
    category_name_list = []
    for bookmark in bookmark_list:
        category_name_list.append(bookmark['category_name'])
    category_name_list = list(set(category_name_list))

    # カテゴリ、ブックマークを登録
    angle_cnt = 1
    angle_judge_cnt = len(category_name_list) / 3
    for c_idx, category_name in enumerate(category_name_list):
        c_idx += 1

        if not c_idx % angle_judge_cnt:
            angle_cnt += 1
            angle_cnt = min(angle_cnt, 3)
        category = Category.objects.create(
            user_id=user.id,
            name=category_name,
            angle=angle_cnt,
            tag_open=0,
            sort=c_idx,
        )

        for b_idx, bookmark in enumerate(bookmark_list):
            b_idx += 1
            if bookmark['category_name'] == category_name and len(bookmark['url']) <= 255:
                Bookmark.objects.create(
                    user_id=user.pk,
                    name=bookmark['a_name'],
                    url=url_exchnge(bookmark['url']),
                    category_id=category.id,
                    sort=b_idx,
                )
