# -*- coding: utf-8 -*-

import re
from django.http import HttpResponse
from django.utils import simplejson
from module.misc.get_pagetitle import getPageTitle
from module.misc.get_googlesuggest import GetGoogleSuggest
from module.oauth.decorator import require_user
from module.setting.models import Category


@require_user
def get_page_title(request):
    '''
    URLからタイトルを取得
    '''
    if request.method == 'POST':
        url = request.POST['url']
        r = re.compile(r"^https?://")
        if not r.match(url):
            url = "http://%s" % url
        title = getPageTitle(url)
        if title:
            r = re.compile(r"^\s+")
            title = r.sub('', title)
            ret_json = {"result": True, "title": title}
        else:
            ret_json = {"result": False}
        json = simplejson.dumps(ret_json, ensure_ascii=False)
        return HttpResponse(json, mimetype='applicatlion/json')


@require_user
def tag_open(request):
    '''
    カテゴリタブの開閉を記録する
    '''
    if request.method == 'POST':
        r = re.compile(r"h2-")
        category_id = r.sub('', request.POST['category_id'])
        category = Category.get_cache(category_id)
        if category.tag_open:
            category.tag_open = False
        else:
            category.tag_open = True
        category.sync_flag = True
        category.save()
        return HttpResponse()


@require_user
def update_color(request):
    '''
    カテゴリ背景色の更新を記録
    '''
    if request.method == 'POST':
        r1 = re.compile(r"item-")
        r2 = re.compile(r"color-")
        category_id = r1.sub('', request.POST['category_id'])
        color_id = r2.sub('', request.POST['color'])
        category = Category.get_cache(category_id)
        category.color_id = color_id
        category.sync_flag = True
        category.save()
        return HttpResponse()


@require_user
def swap_category(request):
    '''
    カテゴリの位置更新を記録
    '''
    if request.method == 'POST':
        update_col = {'column-1': request.POST['column-1'],
                      'column-2': request.POST['column-2'],
                      'column-3': request.POST['column-3']}
        beginColumn = request.POST['beginColumn']
        beginRow = request.POST['beginRow']
        otherColumnFlg = request.POST['otherColumnFlg']
        r = re.compile(r"column-")
        r1 = re.compile(r",$")
        r2 = re.compile(r"item-")

        # 移動元、移動先どちらの更新か判定
        user = request.user
        if user.page_id:
            page = user.page
            angle_ids_str_list = []
            sort_ids_str_list = []
            for columns, category_ids in update_col.iteritems():
                angle_id = r.sub('', columns)
                if category_ids:
                    update_col = r2.sub('', category_ids)
                    for i, category_id in enumerate(update_col.split(','), 1):
                        angle_ids_str_list.append(u'{}:{}'.format(category_id, angle_id))
                        sort_ids_str_list.append(u'{}:{}'.format(category_id, i))
            page.angle_ids_str = ','.join(angle_ids_str_list)
            page.sort_ids_str = ','.join(sort_ids_str_list)
            page.sync_flag = True
            page.save()
        else:
            if otherColumnFlg == 'true':
                # 移動先
                for columns, category_ids in update_col.iteritems():
                    if columns != beginColumn:
                        category_ids = category_ids + ','
                        if re.search(beginRow + ",", category_ids):
                            angle_id = r.sub('', columns)
                            category_ids = r1.sub('', category_ids)
                            _portal_update(category_ids, angle_id, user)
            else:
                # 移動元
                angle_id = r.sub('', beginColumn)
                _portal_update(update_col[beginColumn], angle_id, user)
        return HttpResponse()


def _portal_update(columns, angle_id, user):
    '''
    カテゴリの位置更新処理
    '''
    r = re.compile(r"item-")
    update_col = r.sub('', columns)
    for i, category_id in enumerate(update_col.split(',')):
        category = Category.get_cache(category_id)
        category.angle = angle_id
        category.sort = i + 1
        category.sync_flag = True
        category.save()


@require_user
def get_sugetst(request):
    '''
    googleサジェストを取得
    '''
    if request.method == 'GET':
        search_text = request.GET['input']
        search_text = search_text.encode("utf-8")
        obj_xml = GetGoogleSuggest(search_text, 10)
        data_list = obj_xml.get_data()
        ret_json = {'results': data_list}
        json = simplejson.dumps(ret_json, ensure_ascii=False)
        return HttpResponse(json, mimetype='applicatlion/json')
