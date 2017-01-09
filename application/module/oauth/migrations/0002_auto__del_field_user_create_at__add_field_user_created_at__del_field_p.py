# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.create_at'
        db.delete_column('oauth_user', 'create_at')

        # Adding field 'User.created_at'
        db.add_column('oauth_user', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 2, 10, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Passport.update_at'
        db.delete_column('oauth_passport', 'update_at')

        # Adding field 'Passport.updated_at'
        db.add_column('oauth_passport', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 2, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding index on 'Passport', fields ['passport']
        db.create_index('oauth_passport', ['passport'])


    def backwards(self, orm):
        # Removing index on 'Passport', fields ['passport']
        db.delete_index('oauth_passport', ['passport'])


        # User chose to not deal with backwards NULL issues for 'User.create_at'
        raise RuntimeError("Cannot reverse this migration. 'User.create_at' and its values cannot be restored.")
        # Deleting field 'User.created_at'
        db.delete_column('oauth_user', 'created_at')


        # User chose to not deal with backwards NULL issues for 'Passport.update_at'
        raise RuntimeError("Cannot reverse this migration. 'Passport.update_at' and its values cannot be restored.")
        # Deleting field 'Passport.updated_at'
        db.delete_column('oauth_passport', 'updated_at')


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
            'access_token_key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'access_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_dir': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['oauth']