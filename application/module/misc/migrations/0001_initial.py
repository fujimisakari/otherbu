# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExceptionTraceback'
        db.create_table('misc_exceptiontraceback', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, db_index=True, blank=True)),
            ('view_name', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, blank=True)),
            ('request_path', self.gf('django.db.models.fields.CharField')(default=None, max_length=1024, blank=True)),
            ('exception_type', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, blank=True)),
            ('exception_message', self.gf('django.db.models.fields.TextField')(default=None, blank=True)),
            ('traceback_log', self.gf('django.db.models.fields.TextField')(default=None, blank=True)),
            ('post_data', self.gf('django.db.models.fields.TextField')(default=None, blank=True)),
        ))
        db.send_create_signal('misc', ['ExceptionTraceback'])


    def backwards(self, orm):
        # Deleting model 'ExceptionTraceback'
        db.delete_table('misc_exceptiontraceback')


    models = {
        'misc.exceptiontraceback': {
            'Meta': {'object_name': 'ExceptionTraceback'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'exception_message': ('django.db.models.fields.TextField', [], {'default': 'None', 'blank': 'True'}),
            'exception_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_data': ('django.db.models.fields.TextField', [], {'default': 'None', 'blank': 'True'}),
            'request_path': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1024', 'blank': 'True'}),
            'traceback_log': ('django.db.models.fields.TextField', [], {'default': 'None', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'db_index': 'True', 'blank': 'True'}),
            'view_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['misc']