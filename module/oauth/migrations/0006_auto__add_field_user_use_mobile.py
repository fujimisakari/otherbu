# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.use_mobile'
        db.add_column('oauth_user', 'use_mobile',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.use_mobile'
        db.delete_column('oauth_user', 'use_mobile')


    models = {
        'oauth.passport': {
            'Meta': {'unique_together': "(('user_id', 'passport'),)", 'object_name': 'Passport'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passport': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'oauth.user': {
            'Meta': {'unique_together': "(('type', 'type_id'),)", 'object_name': 'User'},
            'access_token_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'access_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'page_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sync_flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'use_mobile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_dir': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['oauth']