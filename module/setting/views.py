# -*- coding: utf-8 -*-

from django.db import transaction
from django.conf import settings
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from module.oauth.decorator import require_user
from module.setting.bookmark_api import get_bookmark_form, b_regist, b_edit, b_delete
from module.setting.category_api import get_category_form, c_regist, c_edit, c_delete
from module.setting.design_api import get_design_form, d_edit
from module.setting.forms import BookmarkFormSet, CategoryFormSet, DesignFormSet


def _session_delete(request, session_keys):
    try:
        for key in session_keys:
            del request.session[key]
    except KeyError:
        pass


def _render(request, user, name, param):
    if name == 'bookmark.html':
        param['title'] = settings.BOOKMARK_TITLE
        param['current_url'] = reverse('bookmark_index')
        param['active_flg'] = 'bookmark'
        param['disp_flg'] = 'true'
    elif name == 'category.html':
        param['title'] = settings.CATEGORY_TITLE
        param['current_url'] = reverse('category_index')
        param['active_flg'] = 'category'
    elif name == 'design.html':
        param['title'] = settings.DESIGN_TITLE
        param['current_url'] = reverse('design_index')
        param['active_flg'] = 'design'
    param['navi_active_flg'] = 'setting'             # ナビゲーションのsettingをアクティブ表示する
    param['body_padding'] = settings.SETTING_BODY_PADDING  # <body>のpadding-topを定義
    ctxt = RequestContext(request, param)
    return render_to_response('setting/{0}'.format(name), ctxt)


@require_user
def bookmark_index(request):
    user = request.user
    params = {
        'search_error': False,
        'is_disp': True,
    }
    if request.session.get('comp_mode', False):
        c_id = int(request.session['c_id'])
        params['comp_mode'] = request.session['comp_mode']
        params['formset'] = get_bookmark_form(user, c_id)
        params['c_id'] = c_id
        session_keys = ['c_id', 'comp_mode']
        _session_delete(request, session_keys)
    else:
        params['is_disp'] = False
        if request.session.get('search_error', False):
            params['search_error'] = True
            del request.session['search_error']

    return _render(request, user, 'bookmark.html', params)


@require_user
def bookmark_search(request):
    if request.POST.get('select_category', False):
        c_id = int(request.POST['select_category'])
        request.session['c_id'] = c_id
        request.session['comp_mode'] = 'search'
    else:
        request.session['search_error'] = True

    return HttpResponseRedirect(reverse('bookmark_index'))


@require_user
@transaction.commit_on_success
def bookmark_regist(request):
    user = request.user
    post_data = {
        'name': request.POST['name'],
        'url': request.POST['url'],
        'select_category': request.POST['select_category'],
    }
    b_regist(user, post_data)
    if request.POST.get('return_url', False):
        return HttpResponseRedirect(request.POST['return_url'])
    return HttpResponseRedirect(reverse('bookmark_index'))


@require_user
@transaction.commit_on_success
def bookmark_edit(request):
    user = request.user
    c_id = int(request.POST['search_category'])
    formset = BookmarkFormSet(request.POST)
    b_edit(user, c_id, formset)
    request.session['c_id'] = c_id
    request.session['comp_mode'] = 'edit'
    return HttpResponseRedirect(reverse('bookmark_index'))


@require_user
@transaction.commit_on_success
def bookmark_delete(request):
    user = request.user
    c_id = int(request.POST['search_category'])
    formset = BookmarkFormSet(request.POST)
    b_delete(user, c_id, formset)
    request.session['c_id'] = c_id
    request.session['comp_mode'] = 'delete'
    return HttpResponseRedirect(reverse('bookmark_index'))


@require_user
def category_index(request):
    user = request.user
    params = {'is_disp': True}

    if request.session.get('comp_mode', False):
        params['comp_mode'] = request.session['comp_mode']
        session_keys = ['comp_mode']
        _session_delete(request, session_keys)
    else:
        params['comp_mode'] = None
    params['formset'] = get_category_form(user)

    return _render(request, user, 'category.html', params)


@require_user
@transaction.commit_on_success
def category_regist(request):
    user = request.user
    post_data = {
        'name': request.POST['name'],
        'angle': request.POST['angle'],
    }
    c_regist(user, post_data)
    if request.POST.get('return_url', False):
        return HttpResponseRedirect(request.POST['return_url'])
    return HttpResponseRedirect(reverse('category_index'))


@require_user
@transaction.commit_on_success
def category_edit(request):
    user = request.user
    formset = CategoryFormSet(request.POST)
    c_edit(user, formset)
    request.session['comp_mode'] = 'edit'
    return HttpResponseRedirect(reverse('category_index'))


@require_user
@transaction.commit_on_success
def category_delete(request):
    user = request.user
    formset = CategoryFormSet(request.POST)
    c_delete(user, formset)
    request.session['comp_mode'] = 'delete'
    return HttpResponseRedirect(reverse('category_index'))


@require_user
def design_index(request):
    user = request.user
    params = {'is_disp': True}

    if request.session.get('comp_mode', False):
        params['comp_mode'] = request.session['comp_mode']
        session_keys = ['comp_mode']
        _session_delete(request, session_keys)
    else:
        params['comp_mode'] = None
    params['formset'] = get_design_form(user)
    return _render(request, user, 'design.html', params)


@require_user
@transaction.commit_on_success
def design_edit(request):
    user = request.user
    if request.method == 'POST':
        formset = DesignFormSet(request.POST, request.FILES)
        if formset.is_valid():
            d_edit(request, user, formset)
            request.session['comp_mode'] = 'edit'
        return HttpResponseRedirect(reverse('design_index'))
    else:
        return HttpResponseRedirect(reverse('design_index'))
