# -*- coding: utf-8 -*-

from module.setting.forms import BookmarkFormSet
from module.setting.models import Bookmark
from module.misc.common_api import url_exchnge


def get_bookmark_form(user, c_id):
    bookmark_list = Bookmark.objects.filter(user_id=user.pk, category_id=c_id, del_flg=False).order_by('sort')
    form_bookmark = []
    for bookmark in bookmark_list:
        d = {}
        d['name'] = bookmark.name
        d['id'] = bookmark.id
        d['sort'] = bookmark.sort
        d['url'] = bookmark.url
        form_bookmark.append(d)
    return BookmarkFormSet(initial=form_bookmark, auto_id=False)


def b_regist(user, post_data):

    def get_next_sort_count(user, c_id):
        return Bookmark.objects.filter(user_id=user.pk, category_id=c_id, del_flg=False).count() + 1

    Bookmark.objects.create(
        user_id=user.pk,
        name=post_data['name'],
        url=url_exchnge(post_data['url']),
        category_id=post_data['select_category'],
        sort=get_next_sort_count(user, post_data['select_category']),
    )


def b_move(user, post_data):
    for bookmark in user.bookmark_list:
        if bookmark.id in post_data['bookmark_ids']:
            bookmark.category_id = post_data['after_category_id']
            bookmark.save()


def b_edit(user, c_id, formset):
    if formset.is_valid():
        for c_data in formset.cleaned_data:
            bookmark = Bookmark.objects.get(user_id=user.pk, id=c_data['id'])
            bookmark.name = c_data['name']
            bookmark.url = url_exchnge(c_data['url'])
            bookmark.sort = c_data['sort']
            bookmark.save()


def b_delete(user, c_id, formset):
    if formset.is_valid():
        for c_data in formset.cleaned_data:
            if c_data['del_flg']:
                bookmark = Bookmark.objects.get(user_id=user.pk, id=c_data['id'])
                bookmark.del_flg = True
                bookmark.save()
