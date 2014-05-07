# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.text'
        db.add_column(u'haupt_post', 'text',
                      self.gf('django.db.models.fields.TextField')(default=' '),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.text'
        db.delete_column(u'haupt_post', 'text')


    models = {
        u'haupt.post': {
            'Meta': {'object_name': 'Post'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'alias'", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'title'", 'max_length': '255'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "' '"})
        }
    }

    complete_apps = ['haupt']