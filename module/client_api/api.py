# -*- coding: utf-8 -*-

import datetime
import re

from django.db import transaction

from module.oauth.models import User
from module.setting.models import Category, Bookmark, Page, Design


def delete_duplicate_date(reqest_data):
    """
    重複してるデータを消す
    """
    # 削除するデータIDを取得
    delete_id_list = [k for k, _ in reqest_data['delete'].items()]

    # 削除するデータは更新リストには存在しないようにする
    reqest_data['update'] = {k: v for k, v in reqest_data['update'].items() if k not in delete_id_list}

    # 新規追加するデータが更新リストに存在している場合は、更新リストの情報を新規追加として扱う
    update_dict = {}
    for data_id, data in reqest_data['update'].items():
        if data_id in reqest_data['insert']:
            reqest_data['insert'][data_id] = data
        else:
            update_dict[data_id] = data
    reqest_data['update'] = update_dict

    # 新規追加と削除のリストに重複して存在するデータは、共に消す
    for data_id in delete_id_list:
        if data_id in reqest_data['insert']:
            del reqest_data['insert'][data_id]
            del reqest_data['delete'][data_id]

    return reqest_data


def insert_date(reqest_data, delete_category_id_list):
    """
    Clentの新規データを書き込む
    """
    user_id = reqest_data['User']['id']

    # カテゴリを追加
    category_map = _insert_category(user_id, reqest_data['Category']['insert'])

    # Bookmarkを追加
    bookmark_map = _insert_bookmark(user_id, reqest_data['Bookmark']['insert'], category_map)

    # Pageを追加
    page_map = _insert_page(user_id, reqest_data['Page']['insert'], category_map, delete_category_id_list)

    insert_data_dict = {'Category': category_map, 'Bookmark': bookmark_map, 'Page': page_map}
    return insert_data_dict


def _insert_category(user_id, insert_data):
    cateogry_id_list = []
    create_cateogry_data = []

    for data_id, data in insert_data.items():
        data = Category(user_id=int(user_id), mobile_id=data['id'], name=data['name'], angle=int(data['angle']), sort=int(data['sort']),
                        color_id=int(data['color_id']), tag_open=int(data['tag_open']), sync_flag=False)
        create_cateogry_data.append(data)
        cateogry_id_list.append(data_id)

    Category.objects.bulk_create(create_cateogry_data)
    inserted_category = Category.objects.filter(mobile_id__in=cateogry_id_list)
    category_map = {category.mobile_id: category.to_dict() for category in inserted_category}
    return category_map


def _insert_bookmark(user_id, insert_data, category_map):
    bookmark_id_list = []
    create_bookmark_data = []
    for data_id, data in insert_data.items():
        category_id = category_map[data['category_id']]['id']
        bookmark = Bookmark(user_id=int(user_id), mobile_id=data['id'], category_id=category_id, name=data['name'],
                            url=data['url'], sort=int(data['sort']), sync_flag=False)
        create_bookmark_data.append(bookmark)
        bookmark_id_list.append(data_id)

    Bookmark.objects.bulk_create(create_bookmark_data)
    inserted_bookmark = Bookmark.objects.filter(mobile_id__in=bookmark_id_list)
    bookmark_map = {bookmark.mobile_id: bookmark.to_dict() for bookmark in inserted_bookmark}
    return bookmark_map


def _insert_page(user_id, insert_data, category_map, delete_category_id_list):
    page_id_list = []
    create_page_data = []
    for data_id, data in insert_data.items():
        # pageにClientで作成されたIDを保持してる場合は,DBで生成されたIDに差し替える
        for mobile_id, category in category_map.items():
            data['category_ids_str'] = data['category_ids_str'].replace(str(mobile_id), str(category['id']))
            data['angle_ids_str'] = data['angle_ids_str'].replace(str(mobile_id), str(category['id']))
            data['sort_ids_str'] = data['sort_ids_str'].replace(str(mobile_id), str(category['id']))

        data = Page(user_id=int(user_id), mobile_id=data['id'], name=data['name'], category_ids_str=data['category_ids_str'],
                    angle_ids_str=data['angle_ids_str'], sort_ids_str=data['sort_ids_str'], sync_flag=False)

        # 削除されたCategory情報を保持しないようにする
        def _deta_format(id_str):
            str_list = []
            ids = id_str.split(',')
            for id_str in ids:
                alist = id_str.split(':')
                category_id = alist[0]
                value = alist[1]
                if category_id not in delete_category_id_list:
                    str_list.append('{}:{}'.format(category_id, value))
            return str_list

        # カテゴリ
        category_id_list = data.category_ids_str.split(',')
        data.category_ids_str = ','.join([str(category_id) for category_id in category_id_list if category_id not in delete_category_id_list])
        # アングル
        data.angle_ids_str = ','.join(_deta_format(data.angle_ids_str))
        # 順番
        data.sort_ids_str = ','.join(_deta_format(data.sort_ids_str))

        create_page_data.append(data)
        page_id_list.append(data_id)

    Page.objects.bulk_create(create_page_data)
    inserted_page = Page.objects.filter(mobile_id__in=page_id_list)
    page_map = {page.mobile_id: page.to_dict() for page in inserted_page}
    return page_map


def update_date(request_data, response_data_dict):
    """
    Clentデータの更新
    """
    update_dict = {}
    user_id = request_data['User']['id']

    # user
    user = User.objects.get(id=user_id)
    update_user = request_data['User']
    page_id = request_data['User']['page_id']
    date = str(update_user['updated_at']).split(',')
    date = [int(x) for x in date]
    update_at = datetime.datetime(date[0], date[1], date[2], date[3], date[4], date[5])

    if user.updated_at > update_at:
        page_map = response_data_dict['Page']
        if page_map.get(page_id, False):
            user.page_id = page_map.get(page_id)
        else:
            user.page_id = page_id
        user.use_mobile = True
        user.save()
    update_dict['user'] = user.to_dict()

    # category
    response_data_dict['Category'].update({x.id: x.to_dict() for x in user.no_cache_all_category_list if x.sync_flag})
    Category.objects.filter(user_id=user_id).update(sync_flag=True)

    # bookmark
    response_data_dict['Bookmark'].update({x.id: x.to_dict() for x in user.no_cache_bookmark_list if x.sync_flag})
    Bookmark.objects.filter(user_id=user_id).update(sync_flag=True)

    # Page
    response_data_dict['Page'].update({x.id: x.to_dict() for x in user.no_cache_page_list if x.sync_flag})
    Page.objects.filter(user_id=user_id).update(sync_flag=True)

    # design
    design = Design.objects.get(user_id=user_id)
    update_design = request_data['Design']
    if update_design:
        date = update_design['updated_at'].split(',')
        date = [int(x) for x in date]
        update_at = datetime.datetime(date[0], date[1], date[2], date[3], date[4], date[5])

        if design.updated_at > update_at:
            design.category_back_color = update_design['category_back_color']
            design.link_color = update_design['link_color']
            design.save()
        update_dict['design'] = design.to_dict()
    else:
        update_dict['design'] = {}

    return update_dict
