# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'User.access_token_key'
        db.alter_column('oauth_user', 'access_token_key', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'User.access_token_secret'
        db.alter_column('oauth_user', 'access_token_secret', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'User.access_token_key'
        db.alter_column('oauth_user', 'access_token_key', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'User.access_token_secret'
        db.alter_column('oauth_user', 'access_token_secret', self.gf('django.db.models.fields.CharField')(max_length=200))

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
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_dir': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['oauth']