# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Bookmark.mobile_id'
        db.add_column('setting_bookmark', 'mobile_id',
                      self.gf('django.db.models.fields.CharField')(max_length=100, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Bookmark.sync_flag'
        db.add_column('setting_bookmark', 'sync_flag',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Bookmark.updated_at'
        db.add_column('setting_bookmark', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2015, 5, 7, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Page.mobile_id'
        db.add_column('setting_page', 'mobile_id',
                      self.gf('django.db.models.fields.CharField')(max_length=100, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Page.sync_flag'
        db.add_column('setting_page', 'sync_flag',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Page.updated_at'
        db.add_column('setting_page', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2015, 5, 7, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Category.mobile_id'
        db.add_column('setting_category', 'mobile_id',
                      self.gf('django.db.models.fields.CharField')(max_length=100, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.sync_flag'
        db.add_column('setting_category', 'sync_flag',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Category.updated_at'
        db.add_column('setting_category', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2015, 5, 7, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Design.sync_flag'
        db.add_column('setting_design', 'sync_flag',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Design.updated_at'
        db.add_column('setting_design', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2015, 5, 7, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Bookmark.mobile_id'
        db.delete_column('setting_bookmark', 'mobile_id')

        # Deleting field 'Bookmark.sync_flag'
        db.delete_column('setting_bookmark', 'sync_flag')

        # Deleting field 'Bookmark.updated_at'
        db.delete_column('setting_bookmark', 'updated_at')

        # Deleting field 'Page.mobile_id'
        db.delete_column('setting_page', 'mobile_id')

        # Deleting field 'Page.sync_flag'
        db.delete_column('setting_page', 'sync_flag')

        # Deleting field 'Page.updated_at'
        db.delete_column('setting_page', 'updated_at')

        # Deleting field 'Category.mobile_id'
        db.delete_column('setting_category', 'mobile_id')

        # Deleting field 'Category.sync_flag'
        db.delete_column('setting_category', 'sync_flag')

        # Deleting field 'Category.updated_at'
        db.delete_column('setting_category', 'updated_at')

        # Deleting field 'Design.sync_flag'
        db.delete_column('setting_design', 'sync_flag')

        # Deleting field 'Design.updated_at'
        db.delete_column('setting_design', 'updated_at')


    models = {
        'setting.bookmark': {
            'Meta': {'object_name': 'Bookmark'},
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
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
            'mobile_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
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
            'user_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'db_index': 'True'})
        },
        'setting.page': {
            'Meta': {'object_name': 'Page'},
            'angle_ids_str': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'category_ids_str': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sort_ids_str': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sync_flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['setting']