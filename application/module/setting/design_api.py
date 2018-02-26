from django.conf import settings

from module.misc.common_api import get_file_property, uploader
from module.setting.forms import DesignFormSet
from module.setting.models import Design


def get_design_form(user):
    design = Design.get_cache_user(user.id)[0]
    design_dict = {
        'linkmark_flg': design.linkmark_flg,
        'link_color': design.link_color,
        'category_back_color': design.category_back_color,
        'portal_back_kind': design.portal_back_kind,
        'portal_back_color': design.portal_back_color,
        'image_position': design.image_position
    }
    form_design = [design_dict]
    return DesignFormSet(initial=form_design)


def d_edit(request, user, formset):
    for c_data in formset.cleaned_data:
        design = Design.get_cache_user(user.id)[0]
        # イメージ画像をアップロード
        if request.FILES.get('form-0-image_upload', False):
            dir_path = '{}/{}/{}'.format(settings.USER_IMG_DIR, user.type, user.user_dir)
            uploader(dir_path, request, 'form-0-image_upload')
            upfile = request.FILES['form-0-image_upload']
            file_dict = get_file_property(upfile.name)
            design.bk_image_ext = file_dict['ext']
        design.linkmark_flg = c_data['linkmark_flg'] == 'True'
        design.link_color = c_data['link_color']
        design.category_back_color = c_data['category_back_color']
        design.portal_back_kind = c_data['portal_back_kind'] == 'True'
        design.portal_back_color = c_data['portal_back_color']
        design.image_position = c_data['image_position']
        design.sync_flag = True
        design.save()
