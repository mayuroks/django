# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SampleCount'
        db.create_table(u'clrytest_samplecount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'clrytest', ['SampleCount'])


    def backwards(self, orm):
        # Deleting model 'SampleCount'
        db.delete_table(u'clrytest_samplecount')


    models = {
        u'clrytest.samplecount': {
            'Meta': {'object_name': 'SampleCount'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['clrytest']