# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'FsUser'
        db.delete_table('fs_users')

        # Adding model 'FsTier'
        db.create_table('fs_tiers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('queue', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('agent', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'freeswitch', ['FsTier'])

        # Adding model 'FsUser'
        db.create_table('fs_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userid', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, null=True, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, null=True, blank=True)),
            ('accountcode', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, null=True, blank=True)),
            ('user_context', self.gf('django.db.models.fields.CharField')(default=None, max_length=20, null=True, blank=True)),
            ('effective_caller_id_name', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, null=True, blank=True)),
            ('effective_caller_id_number', self.gf('django.db.models.fields.CharField')(default=None, max_length=20, null=True, blank=True)),
            ('callgroup', self.gf('django.db.models.fields.CharField')(default=None, max_length=10, null=True, blank=True)),
            ('max_calls', self.gf('django.db.models.fields.IntegerField')(default=None, max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal(u'freeswitch', ['FsUser'])

        # Adding model 'FsAgent'
        db.create_table('fs_agents', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('system', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('max_no_answer', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('wrap_up_time', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('reject_delay_time', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('busy_delay_time', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_answer_delay_time', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('last_bridge_start', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('last_bridge_end', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('last_offered_call', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('last_status_change', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_answer_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('calls_answered', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('talk_time', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ready_time', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'freeswitch', ['FsAgent'])


    def backwards(self, orm):
        # Adding model 'FsUser'
        db.create_table('fs_users', (
            ('accountcode', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, null=True, blank=True)),
            ('effective_caller_id_name', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, null=True, blank=True)),
            ('user_context', self.gf('django.db.models.fields.CharField')(default=None, max_length=20, null=True, blank=True)),
            ('callgroup', self.gf('django.db.models.fields.CharField')(default=None, max_length=10, null=True, blank=True)),
            ('max_calls', self.gf('django.db.models.fields.IntegerField')(default=None, max_length=2, null=True, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, null=True, blank=True)),
            ('userid', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('effective_caller_id_number', self.gf('django.db.models.fields.CharField')(default=None, max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'freeswitch', ['FsUser'])

        # Deleting model 'FsTier'
        db.delete_table('fs_tiers')

        # Deleting model 'FsUser'
        db.delete_table('fs_users')

        # Deleting model 'FsAgent'
        db.delete_table('fs_agents')


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
            'Meta': {'object_name': 'FsAgent', 'db_table': "'fs_agents'"},
            'busy_delay_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'calls_answered': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'contact': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_bridge_end': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_bridge_start': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_offered_call': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_status_change': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'max_no_answer': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
            'Meta': {'object_name': 'FsTier', 'db_table': "'fs_tiers'"},
            'agent': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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