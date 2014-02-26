# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cdr'
        db.create_table('fs_cdr', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('caller_id_name', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('caller_id_number', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('destination_number', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('context', self.gf('django.db.models.fields.CharField')(default=None, max_length=80, null=True, blank=True)),
            ('start_stamp', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('answer_stamp', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('end_stamp', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('billsec', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('hangup_cause', self.gf('django.db.models.fields.CharField')(default=None, max_length=80, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default=None, max_length=120, null=True, blank=True)),
            ('bleg_uuid', self.gf('django.db.models.fields.CharField')(default=None, max_length=120, null=True, blank=True)),
            ('accountcode', self.gf('django.db.models.fields.CharField')(default=None, max_length=80, null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.CharField')(default=None, max_length=80, null=True, blank=True)),
        ))
        db.send_create_signal(u'freeswitch', ['Cdr'])


    def backwards(self, orm):
        # Deleting model 'Cdr'
        db.delete_table('fs_cdr')


    models = {
        u'freeswitch.cdr': {
            'Meta': {'object_name': 'Cdr', 'db_table': "'fs_cdr'"},
            'accountcode': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'answer_stamp': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'billsec': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'bleg_uuid': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'caller_id_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'caller_id_number': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'context': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'destination_number': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'end_stamp': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'hangup_cause': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_stamp': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['freeswitch']