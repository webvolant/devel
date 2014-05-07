# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'haupt_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='title', max_length=255)),
        ))
        db.send_create_signal(u'haupt', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'haupt_post')


    models = {
        u'haupt.pos': {
            'Meta': {'object_name': 'Pos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nam': ('django.db.models.fields.CharField', [], {'default': "'title'", 'max_length': '255'})
        },
        u'haupt.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'title'", 'max_length': '255'})
        }
    }

    complete_apps = ['haupt']