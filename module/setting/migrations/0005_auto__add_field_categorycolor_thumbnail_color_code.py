# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CategoryColor.thumbnail_color_code'
        db.add_column('setting_categorycolor', 'thumbnail_color_code',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CategoryColor.thumbnail_color_code'
        db.delete_column('setting_categorycolor', 'thumbnail_color_code')


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
            'color_code1': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'color_code2': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'color_code3': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'font_color': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'icon_color': ('django.db.models.fields.CharField', [], {'default': "'white'", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sort': ('django.db.models.fields.IntegerField', [], {}),
            'thumbnail_color_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
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
        },
        'setting.page': {
            'Meta': {'object_name': 'Page'},
            'category_ids_str': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['setting']