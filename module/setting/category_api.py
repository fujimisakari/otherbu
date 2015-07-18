# -*- coding: utf-8 -*-

from module.setting.models import Category, Bookmark
from module.setting.forms import CategoryFormSet


def get_category_form(user):
    category_list = Category.objects.filter(user_id=user.pk).order_by('angle').order_by('sort')
    form_category = []
    for category in category_list:
        d = {}
        d['name'] = category.name
        d['id'] = category.id
        form_category.append(d)
    return CategoryFormSet(initial=form_category, auto_id=False)


def c_regist(user, post_data):

    def get_next_sort_count():
        return Category.objects.filter(user_id=user.pk, angle=post_data['angle']).count() + 1

    category = Category.objects.create(
        user_id=user.pk,
        name=post_data['name'],
        angle=post_data['angle'],
        sort=get_next_sort_count(),
    )
    if user.page_id:
        page = user.page
        page.category_ids_str += u',{}'.format(category.id)
        page.angle_ids_str += u',{}:{}'.format(category.id, post_data['angle'])
        page.sort_ids_str += u',{}:0'.format(category.id)
        page.sync_flag = True
        page.save()


def c_edit(user, formset):
    if formset.is_valid():
        for c_data in formset.cleaned_data:
            try:
                category = Category.objects.get(id=c_data['id'], user_id=user.pk)
            except Category.DoesNotExist:
                return False
            category.name = c_data['name']
            category.sync_flag = True
            category.save()


def c_delete(user, formset):
    if formset.is_valid():
        for c_data in formset.cleaned_data:
            if c_data['del_flg']:
                try:
                    category = Category.objects.get(id=c_data['id'], user_id=user.pk)
                    bookmark_list = Bookmark.objects.filter(user_id=user.pk, category_id=category.id)
                    for bookmark in bookmark_list:
                        user.delete_manager.add_delete_id('bookmark', bookmark.id)
                        bookmark.delete()
                except Category.DoesNotExist:
                    return False
                user.delete_manager.add_delete_id('category', category.id)
                category.delete()
