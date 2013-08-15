# -*- coding: utf-8 -*-

from module.setting.models import Page, Category


def get_page(page_id):
    return Page.get_cache(page_id)


def get_page_category_list(user_id, p_id):
    page = Page.get_cache(p_id)
    if not page.category_ids_str:
        return []
    c_list = Category.get_cache_user(user_id)
    c_list = [c for c in c_list if c.id in page.category_ids]
    angle_dict = page.angle_dict
    sort_dict = page.sort_dict
    for c in c_list:
        if angle_dict:
            c.angle = angle_dict[c.id]
        if sort_dict:
            c.sort = sort_dict[c.id]
    c_list = sorted(c_list, key=lambda x: x.angle)
    c_list = sorted(c_list, key=lambda x: x.sort)
    return c_list


def p_regist(user, post_data):
    category_ids = ''
    angle_ids_str_list = []
    sort_ids_str_list = []
    if post_data['category_ids']:
        category_ids = ','.join(post_data['category_ids'])
        for i, category_id in enumerate(post_data['category_ids'], 1):
            angle_ids_str_list.append(u'{}:{}'.format(category_id, 1))
            sort_ids_str_list.append(u'{}:{}'.format(category_id, i))
    page = Page.objects.create(
        user_id=user.pk,
        name=post_data['name'],
        category_ids_str=category_ids,
        angle_ids_str=u','.join(angle_ids_str_list),
        sort_ids_str=u','.join(sort_ids_str_list),
    )
    user.page_id = page.id
    user.save()


def p_select(user, page_id):
    try:
        page = Page.objects.get(id=page_id)
    except:
        user.page_id = 0
        user.save()
        return
    user.page_id = page.id
    user.save()


def p_edit(user, post_data):
    category_ids = ''
    angle_ids_str_list = []
    sort_ids_str_list = []
    if post_data['category_ids']:
        category_ids = ','.join(post_data['category_ids'])
        for i, category_id in enumerate(post_data['category_ids'], 1):
            angle_ids_str_list.append(u'{}:{}'.format(category_id, 1))
            sort_ids_str_list.append(u'{}:{}'.format(category_id, i))
    page = Page.objects.get(user_id=user.id, id=post_data['page_id'])
    page.name = post_data['name']
    page.category_ids_str = category_ids
    page.angle_ids_str = u','.join(angle_ids_str_list)
    page.sort_ids_str = u','.join(sort_ids_str_list)
    page.save()


def p_delete(user, page_id):
    page = Page.objects.get(user_id=user.id, id=page_id)
    page.delete()
