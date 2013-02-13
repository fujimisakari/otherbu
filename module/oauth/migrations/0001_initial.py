# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('oauth_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('type_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user_dir', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('access_token_key', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('access_token_secret', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('create_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('oauth', ['User'])

        # Adding unique constraint on 'User', fields ['type', 'type_id']
        db.create_unique('oauth_user', ['type', 'type_id'])

        # Adding model 'Passport'
        db.create_table('oauth_passport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('passport', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('update_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('oauth', ['Passport'])

        # Adding unique constraint on 'Passport', fields ['user_id', 'passport']
        db.create_unique('oauth_passport', ['user_id', 'passport'])


    def backwards(self, orm):
        # Removing unique constraint on 'Passport', fields ['user_id', 'passport']
        db.delete_unique('oauth_passport', ['user_id', 'passport'])

        # Removing unique constraint on 'User', fields ['type', 'type_id']
        db.delete_unique('oauth_user', ['type', 'type_id'])

        # Deleting model 'User'
        db.delete_table('oauth_user')

        # Deleting model 'Passport'
        db.delete_table('oauth_passport')


    models = {
        'oauth.passport': {
            'Meta': {'unique_together': "(('user_id', 'passport'),)", 'object_name': 'Passport'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passport': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'update_at': ('django.db.models.fields.DateTimeField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'oauth.user': {
            'Meta': {'unique_together': "(('type', 'type_id'),)", 'object_name': 'User'},
            'access_token_key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'access_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_dir': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['oauth']