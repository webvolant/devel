# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Pos'
        db.delete_table(u'haupt_pos')


    def backwards(self, orm):
        # Adding model 'Pos'
        db.create_table(u'haupt_pos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nam', self.gf('django.db.models.fields.CharField')(default='title', max_length=255)),
        ))
        db.send_create_signal(u'haupt', ['Pos'])


    models = {
        u'haupt.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'title'", 'max_length': '255'})
        }
    }

    complete_apps = ['haupt']