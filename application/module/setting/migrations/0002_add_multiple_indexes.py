# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Category', fields ['user_id']
        db.create_index('setting_bookmark', ['user_id', 'del_flg'])
        db.create_index('setting_bookmark', ['user_id', 'category_id', 'del_flg'])
        db.create_index('setting_category', ['user_id', 'del_flg'])
        db.create_index('setting_category', ['user_id', 'angle', 'del_flg'])

    def backwards(self, orm):
        # Removing index on 'Category', fields ['user_id']
        db.delete_index('setting_bookmark', ['user_id', 'del_flg'])
        db.delete_index('setting_bookmark', ['user_id', 'category_id', 'del_flg'])
        db.delete_index('setting_category', ['user_id', 'del_flg'])
        db.delete_index('setting_category', ['user_id', 'angle', 'del_flg'])

    models = {
        'setting.bookmark': {
            'Meta': {'object_name': 'Bookmark'},
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'del_flg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '200'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'setting.category': {
            'Meta': {'object_name': 'Category'},
            'angle': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'color_id': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'del_flg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tag_open': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'setting.categorycolor': {
            'Meta': {'object_name': 'CategoryColor'},
            'color_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'font_color': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'icon_color': ('django.db.models.fields.CharField', [], {'default': "'white'", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sort': ('django.db.models.fields.IntegerField', [], {})
        },
        'setting.design': {
            'Meta': {'object_name': 'Design'},
            'bk_image_ext': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'category_back_color': ('django.db.models.fields.CharField', [], {'default': "'#FFF'", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_position': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'link_color': ('django.db.models.fields.CharField', [], {'default': "'#005580'", 'max_length': '10'}),
            'linkmark_flg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'portal_back_color': ('django.db.models.fields.CharField', [], {'default': "'#FFF'", 'max_length': '10'}),
            'portal_back_kind': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['setting']
