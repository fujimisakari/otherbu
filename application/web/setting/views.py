# -*- coding: utf-8 -*-

import csv

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from module.oauth.decorator import require_user
from module.setting.bookmark_api import get_bookmark_form, b_regist, b_edit, b_delete, b_move
from module.setting.category_api import get_category_form, c_regist, c_edit, c_delete
from module.setting.design_api import get_design_form, d_edit
from module.setting.forms import BookmarkFormSet, CategoryFormSet, DesignFormSet
from module.setting.import_api import get_import_form, import_proc
from module.setting.page_api import get_page, p_regist, p_delete, p_edit, p_select, get_page_category_list


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
    if name == 'bookmark.html':
        param['title'] = settings.BOOKMARK_MOVE_TITLE
        param['current_url'] = reverse('bookmark_move_index')
        param['active_flg'] = 'bookmark_move'
        param['disp_flg'] = 'true'
    elif name == 'category.html':
        param['title'] = settings.CATEGORY_TITLE
        param['current_url'] = reverse('category_index')
        param['active_flg'] = 'category'
    elif name == 'page.html':
        param['title'] = settings.PAGE_TITLE
        param['current_url'] = reverse('page_index')
        param['active_flg'] = 'page'
    elif name == 'design.html':
        param['title'] = settings.DESIGN_TITLE
        param['current_url'] = reverse('design_index')
        param['active_flg'] = 'design'
    elif name == 'import.html':
        param['title'] = settings.IMPORT_TITLE
        param['current_url'] = reverse('import_index')
        param['active_flg'] = 'import'
    elif name == 'export.html':
        param['title'] = settings.EXPORT_TITLE
        param['current_url'] = reverse('export_index')
        param['active_flg'] = 'export'
    elif name == 'info.html':
        param['title'] = settings.INFO_TITLE
        param['current_url'] = reverse('info_index')
        param['active_flg'] = 'info'
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
    try:
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
    except:
        session_keys = ['c_id', 'comp_mode']
        _session_delete(request, session_keys)
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
def bookmark_move_index(request):
    user = request.user
    params = {
        'search_error': False,
        'is_disp': True,
    }
    try:
        if request.session.get('comp_mode', False):
            c_id = int(request.session['c_id'])
            params['comp_mode'] = request.session['comp_mode']
            params['select_bookmark_list'] = [b for b in user.bookmark_list if b.category_id == c_id]
            params['c_id'] = c_id
            session_keys = ['c_id', 'comp_mode']
            _session_delete(request, session_keys)
        else:
            params['is_disp'] = False
            if request.session.get('search_error', False):
                params['search_error'] = True
                del request.session['search_error']
    except:
        session_keys = ['c_id', 'comp_mode']
        _session_delete(request, session_keys)
    return _render(request, user, 'bookmark_move.html', params)


@require_user
def bookmark_move_search(request):
    if request.POST.get('select_category', False):
        c_id = int(request.POST['select_category'])
        request.session['c_id'] = c_id
        request.session['comp_mode'] = 'search'
    else:
        request.session['search_error'] = True

    return HttpResponseRedirect(reverse('bookmark_move_index'))


@require_user
def bookmark_move_exec(request):
    user = request.user
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('bookmark_move_index'))

    category_id = int(request.POST['category_id'])
    bookmark_ids = [int(i) for i in request.POST.getlist('move_flg')]
    post_data = {
        'after_category_id': request.POST['move_category'],
        'bookmark_ids': bookmark_ids,
    }
    b_move(user, post_data)
    request.session['comp_mode'] = 'move'
    request.session['c_id'] = category_id
    return HttpResponseRedirect(reverse('bookmark_move_index'))


@require_user
def category_index(request):
    user = request.user
    params = {'is_disp': True}

    try:
        if request.session.get('comp_mode', False):
            params['comp_mode'] = request.session['comp_mode']
            session_keys = ['comp_mode']
            _session_delete(request, session_keys)
        else:
            params['comp_mode'] = None
        params['formset'] = get_category_form(user)
    except:
        session_keys = ['comp_mode']
        _session_delete(request, session_keys)
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
def page_index(request):
    user = request.user
    params = {
        'search_error': False,
        'is_disp': True,
        'page_list': user.page_list,
    }
    try:
        if request.session.get('comp_mode', False):
            params['comp_mode'] = request.session['comp_mode']
            if request.session['comp_mode'] == 'delete':
                params['is_disp'] = False
            else:
                page_id = int(request.session['page_id'])
                page_category_list = get_page_category_list(user.id, page_id)
                params['page_category_id_list'] = [pc.id for pc in page_category_list]
                params['page'] = get_page(page_id)
                session_keys = ['page_id', 'comp_mode']
                _session_delete(request, session_keys)
        else:
            params['is_disp'] = False
            if request.session.get('search_error', False):
                params['search_error'] = True
                del request.session['search_error']
    except:
        session_keys = ['page_id', 'comp_mode']
        _session_delete(request, session_keys)
    return _render(request, user, 'page.html', params)


@require_user
def page_search(request):
    if request.POST.get('select_page', False):
        page_id = int(request.POST['select_page'])
        request.session['page_id'] = page_id
        request.session['comp_mode'] = 'search'
    else:
        request.session['search_error'] = True

    return HttpResponseRedirect(reverse('page_index'))


@require_user
@transaction.commit_on_success
def page_select(request, page_id):
    user = request.user
    page_id = int(page_id)
    p_select(user, page_id)
    return HttpResponseRedirect(reverse('portal_index'))


@require_user
@transaction.commit_on_success
def page_regist(request):
    user = request.user
    post_data = {
        'name': request.POST['name'],
        'category_ids': request.POST.getlist('regist_flg'),
    }
    p_regist(user, post_data)
    if request.POST.get('return_url', False):
        return HttpResponseRedirect(request.POST['return_url'])
    return HttpResponseRedirect(reverse('page_index'))


@require_user
@transaction.commit_on_success
def page_edit(request):
    user = request.user
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('page_index'))

    page_id = int(request.POST['page_id'])
    post_data = {
        'page_id': page_id,
        'name': request.POST['name'],
        'category_ids': request.POST.getlist('regist_flg'),
    }
    p_edit(user, post_data)
    request.session['comp_mode'] = 'edit'
    request.session['page_id'] = page_id
    return HttpResponseRedirect(reverse('page_index'))


@require_user
@transaction.commit_on_success
def page_delete(request):
    user = request.user
    if not request.POST.get('page_id', False):
        return HttpResponseRedirect(reverse('page_index'))

    page_id = int(request.POST.get('page_id'))
    p_delete(user, page_id)
    request.session['comp_mode'] = 'delete'
    return HttpResponseRedirect(reverse('page_index'))


@require_user
def design_index(request):
    user = request.user
    params = {'is_disp': True}

    try:
        if request.session.get('comp_mode', False):
            params['comp_mode'] = request.session['comp_mode']
            session_keys = ['comp_mode']
            _session_delete(request, session_keys)
        else:
            params['comp_mode'] = None
        params['formset'] = get_design_form(user)
    except:
        session_keys = ['comp_mode']
        _session_delete(request, session_keys)
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


@require_user
def import_index(request):
    user = request.user
    params = {'is_disp': True}
    try:
        if request.session.get('comp_mode', False):
            params['comp_mode'] = request.session['comp_mode']
            session_keys = ['comp_mode']
            _session_delete(request, session_keys)
        else:
            params['comp_mode'] = None
        params['formset'] = get_import_form()
    except:
        session_keys = ['comp_mode']
        _session_delete(request, session_keys)
    return _render(request, user, 'import.html', params)


@require_user
@transaction.commit_on_success
def import_exec(request):
    user = request.user
    if request.method == 'POST':
        if not request.FILES.get('form-0-bookmark_upload', False):
            return HttpResponseRedirect(reverse('import_index'))
        try:
            import_proc(request, user)
        except:
            return HttpResponseRedirect(reverse('import_index'))
        request.session['comp_mode'] = 'import'
        return HttpResponseRedirect(reverse('import_index'))
    else:
        return HttpResponseRedirect(reverse('import_index'))


@require_user
def export_index(request):
    user = request.user
    return _render(request, user, 'export.html', {})


@require_user
def export_exec(request):
    user = request.user

    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=otherbu_bookmark.csv'

    encode_type = 'cp932'
    writer = csv.writer(response)
    writer.writerow([u'カテゴリ'.encode(encode_type), u'ブックマーク'.encode(encode_type), u'URL'.encode(encode_type)])
    bookmark_list = sorted(user.bookmark_list, key=lambda x: x.category_id)
    for bookmark in bookmark_list:
        try:
            category_name = bookmark.category.name.encode(encode_type)
        except:
            category_name = bookmark.category.name.encode('utf-8')

        try:
            bookmark_name = bookmark.name.encode('cp932')
        except:
            bookmark_name = bookmark.name.encode('utf-8')
        writer.writerow([category_name, bookmark_name, bookmark.url])
    return response


@require_user
def info_index(request):
    user = request.user
    return _render(request, user, 'info.html', {})
