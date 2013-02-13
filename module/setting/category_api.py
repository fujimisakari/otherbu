# -*- coding: utf-8 -*-

from module.setting.models import Category
from module.setting.forms import CategoryFormSet


def get_category_form(user):
    category_list = Category.objects.filter(user_id=user.pk, del_flg=False).order_by('angle').order_by('sort')
    form_category = []
    for category in category_list:
        d = {}
        d['name'] = category.name
        d['id'] = category.id
        form_category.append(d)
    return CategoryFormSet(initial=form_category, auto_id=False)


def c_regist(user, post_data):

    def get_next_sort_count():
        return Category.objects.filter(user_id=user.pk, angle=post_data['angle'], del_flg=False).count() + 1

    Category.objects.create(
        user_id=user.pk,
        name=post_data['name'],
        angle=post_data['angle'],
        sort=get_next_sort_count(),
    )


def c_edit(user, formset):
    if formset.is_valid():
        for c_data in formset.cleaned_data:
            try:
                category = Category.objects.get(id=c_data['id'], user_id=user.pk)
            except Category.DoesNotExist:
                return False
            category.name = c_data['name']
            category.save()


def c_delete(user, formset):
    if formset.is_valid():
        for c_data in formset.cleaned_data:
            if c_data['del_flg']:
                try:
                    category = Category.objects.get(id=c_data['id'], user_id=user.pk)
                except Category.DoesNotExist:
                    return False
                category.del_flg = True
                category.save()
