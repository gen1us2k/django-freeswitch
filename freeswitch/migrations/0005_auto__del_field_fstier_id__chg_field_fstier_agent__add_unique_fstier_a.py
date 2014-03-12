# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'FsTier.id'
        db.delete_column('fs_tiers', u'id')


        # Changing field 'FsTier.agent'
        db.alter_column('tiers', 'agent', self.gf('django.db.models.fields.CharField')(default='', max_length=255, primary_key=True))
        # Adding unique constraint on 'FsTier', fields ['agent']
        db.create_unique('tiers', ['agent'])

        # Deleting field 'FsAgent.id'
        db.delete_column('fs_agents', u'id')


        # Changing field 'FsAgent.name'
        db.alter_column('agents', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=255, primary_key=True))
        # Adding unique constraint on 'FsAgent', fields ['name']
        db.create_unique('agents', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'FsAgent', fields ['name']
        db.delete_unique('agents', ['name'])

        # Removing unique constraint on 'FsTier', fields ['agent']
        db.delete_unique('tiers', ['agent'])

        # Adding field 'FsTier.id'
        db.add_column('fs_tiers', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)


        # Changing field 'FsTier.agent'
        db.alter_column('tiers', 'agent', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))
        # Adding field 'FsAgent.id'
        db.add_column('fs_agents', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)


        # Changing field 'FsAgent.name'
        db.alter_column('agents', 'name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

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
        },
        u'freeswitch.fsagent': {
            'Meta': {'object_name': 'FsAgent', 'db_table': "'agents'"},
            'busy_delay_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'calls_answered': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'contact': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_bridge_end': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_bridge_start': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_offered_call': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_status_change': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'max_no_answer': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'primary_key': 'True'}),
            'no_answer_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'no_answer_delay_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ready_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reject_delay_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'system': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'talk_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'wrap_up_time': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'freeswitch.fstier': {
            'Meta': {'object_name': 'FsTier', 'db_table': "'tiers'"},
            'agent': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'queue': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'freeswitch.fsuser': {
            'Meta': {'object_name': 'FsUser', 'db_table': "'fs_users'"},
            'accountcode': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'callgroup': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'effective_caller_id_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'effective_caller_id_number': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_calls': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user_context': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'userid': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['freeswitch']