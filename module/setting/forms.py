# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.forms.formsets import formset_factory
from module.misc.common_api import get_file_property


class BookmarkForm(forms.Form):
    name = forms.CharField(max_length=200,
                           widget=forms.TextInput(attrs={'class': 'input-bookmark focused'}))
    id = forms.IntegerField(widget=forms.HiddenInput)
    url = forms.CharField(max_length=200,
                          widget=forms.TextInput(attrs={'class': 'input-url focused'}))
    sort = forms.IntegerField(widget=forms.HiddenInput)
    del_flg = forms.BooleanField(required=False)


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=200,
                           widget=forms.TextInput(attrs={'class': 'input-category focused'}))
    id = forms.IntegerField(widget=forms.HiddenInput)
    del_flg = forms.BooleanField(required=False)


class DesignForm(forms.Form):
    LINKMARK_CHOICES = ((False, u'黒'), (True, u'白'))
    PORTAL_KIND_CHOICES = ((False, u'背景色'), (True, u'背景画像'))
    PORTAL_BACK_CHOICES = (('no-repeat', u'画像を引き伸ばして全体表示'), ('repeat', u'画像を繰り返し表示'), ('original', u'画像をそのままのサイズで表示'))

    linkmark_flg = forms.ChoiceField(initial=False, choices=LINKMARK_CHOICES, widget=forms.RadioSelect)
    link_color = forms.CharField(initial='#005580', max_length=7,
                                 widget=forms.TextInput(attrs={'class': 'input-small focused'}))
    category_back_color = forms.CharField(initial='#ffffff', max_length=7,
                                          widget=forms.TextInput(attrs={'class': 'input-small focused'}))
    portal_back_kind = forms.ChoiceField(initial=False, choices=PORTAL_KIND_CHOICES, widget=forms.RadioSelect)
    portal_back_color = forms.CharField(initial='#ffffff', max_length=7,
                                        widget=forms.TextInput(attrs={'class': 'input-small focused'}))
    image_upload = forms.FileField(required=False)
    image_position = forms.ChoiceField(initial='no-repeat', choices=PORTAL_BACK_CHOICES)

    def clean_image_upload(self):
        upfile = self.cleaned_data['image_upload']
        if upfile:
            # ファイルのサイズチェック
            if upfile.size > settings.UPLOAD_SIZE_LIMIT:
                raise forms.ValidationError(u'データサイズが2Mを超てます')

            # 拡張子チェック
            allow_ext = ['jpeg', 'png', 'gif', 'jpg']
            file_dict = get_file_property(upfile.name)
            if file_dict is not None:
                if not file_dict['ext'].lower() in allow_ext:
                    raise forms.ValidationError(u'この%sの拡張子は使用できません' % file_dict['ext'])
            else:
                raise forms.ValidationError(u'拡張子が不明です')


class ImportForm(forms.Form):
    bookmark_upload = forms.FileField()


BookmarkFormSet = formset_factory(BookmarkForm, extra=0)
CategoryFormSet = formset_factory(CategoryForm, extra=0)
DesignFormSet = formset_factory(DesignForm, max_num=1)
ImportFormSet = formset_factory(ImportForm)
