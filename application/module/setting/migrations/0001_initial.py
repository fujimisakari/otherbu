# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('setting_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('angle', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('color_id', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('tag_open', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('del_flg', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('setting', ['Category'])

        # Adding model 'CategoryColor'
        db.create_table('setting_categorycolor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('color_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('font_color', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('icon_color', self.gf('django.db.models.fields.CharField')(default='white', max_length=10)),
            ('sort', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('setting', ['CategoryColor'])

        # Adding model 'Bookmark'
        db.create_table('setting_bookmark', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('category_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(default=0, max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('del_flg', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('setting', ['Bookmark'])

        # Adding model 'Design'
        db.create_table('setting_design', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(unique=True, db_index=True)),
            ('linkmark_flg', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('link_color', self.gf('django.db.models.fields.CharField')(default='#005580', max_length=10)),
            ('category_back_color', self.gf('django.db.models.fields.CharField')(default='#FFF', max_length=10)),
            ('portal_back_kind', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('portal_back_color', self.gf('django.db.models.fields.CharField')(default='#FFF', max_length=10)),
            ('image_position', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('bk_image_ext', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
        ))
        db.send_create_signal('setting', ['Design'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('setting_category')

        # Deleting model 'CategoryColor'
        db.delete_table('setting_categorycolor')

        # Deleting model 'Bookmark'
        db.delete_table('setting_bookmark')

        # Deleting model 'Design'
        db.delete_table('setting_design')


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