# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Category', fields ['mobile_id']
        db.delete_unique('setting_category', ['mobile_id'])

        # Removing unique constraint on 'Page', fields ['mobile_id']
        db.delete_unique('setting_page', ['mobile_id'])

        # Removing unique constraint on 'Bookmark', fields ['mobile_id']
        db.delete_unique('setting_bookmark', ['mobile_id'])

        # Adding model 'DeleteManager'
        db.create_table('setting_deletemanager', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('bookmark', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('page', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('setting', ['DeleteManager'])


        # Changing field 'Page.angle_ids_str'
        db.alter_column('setting_page', 'angle_ids_str', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Page.category_ids_str'
        db.alter_column('setting_page', 'category_ids_str', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Page.sort_ids_str'
        db.alter_column('setting_page', 'sort_ids_str', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Adding index on 'Design', fields ['user_id']
        db.create_index('setting_design', ['user_id'])

        # Deleting model 'DeleteManager'
        db.delete_table('setting_deletemanager')

        # Adding unique constraint on 'Bookmark', fields ['mobile_id']
        db.create_unique('setting_bookmark', ['mobile_id'])

        # Adding unique constraint on 'Page', fields ['mobile_id']
        db.create_unique('setting_page', ['mobile_id'])


        # Changing field 'Page.angle_ids_str'
        db.alter_column('setting_page', 'angle_ids_str', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Page.category_ids_str'
        db.alter_column('setting_page', 'category_ids_str', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Page.sort_ids_str'
        db.alter_column('setting_page', 'sort_ids_str', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))
        # Adding unique constraint on 'Category', fields ['mobile_id']
        db.create_unique('setting_category', ['mobile_id'])


    models = {
        'setting.bookmark': {
            'Meta': {'object_name': 'Bookmark'},
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '200'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sync_flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'setting.category': {
            'Meta': {'object_name': 'Category'},
            'angle': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'color_id': ('django.db.models.fields.IntegerField', [], {'default': '18'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sync_flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tag_open': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
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
        'setting.deletemanager': {
            'Meta': {'object_name': 'DeleteManager'},
            'bookmark': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
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
            'sync_flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        'setting.page': {
            'Meta': {'object_name': 'Page'},
            'angle_ids_str': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'category_ids_str': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sort_ids_str': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sync_flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['setting']
