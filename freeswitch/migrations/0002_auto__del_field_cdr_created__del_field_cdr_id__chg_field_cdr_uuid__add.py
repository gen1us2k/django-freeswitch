# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Cdr.created'
        db.delete_column('fs_cdr', 'created')

        # Deleting field 'Cdr.id'
        db.delete_column('fs_cdr', u'id')


        # Changing field 'Cdr.uuid'
        db.alter_column('fs_cdr', 'uuid', self.gf('django.db.models.fields.CharField')(default='', max_length=120, primary_key=True))
        # Adding unique constraint on 'Cdr', fields ['uuid']
        db.create_unique('fs_cdr', ['uuid'])


    def backwards(self, orm):
        # Removing unique constraint on 'Cdr', fields ['uuid']
        db.delete_unique('fs_cdr', ['uuid'])

        # Adding field 'Cdr.created'
        db.add_column('fs_cdr', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None, blank=True),
                      keep_default=False)

        # Adding field 'Cdr.id'
        db.add_column('fs_cdr', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)


        # Changing field 'Cdr.uuid'
        db.alter_column('fs_cdr', 'uuid', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

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
            'destination_number': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'end_stamp': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'hangup_cause': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'start_stamp': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'primary_key': 'True'})
        }
    }

    complete_apps = ['freeswitch']