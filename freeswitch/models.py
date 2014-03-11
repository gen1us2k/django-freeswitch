# coding=utf-8
from django.db import models


class Cdr(models.Model):
    caller_id_name = models.CharField(max_length=50, null=True, blank=True, default=None)
    caller_id_number = models.CharField(max_length=50, null=True, blank=True, default=None)
    destination_number = models.CharField(max_length=50, null=True, blank=True, default=None)
    context = models.CharField(max_length=80, null=True, blank=True, default=None)
    start_stamp = models.DateTimeField(null=True, blank=True, default=None)
    answer_stamp = models.DateTimeField(null=True, blank=True, default=None)
    end_stamp = models.DateTimeField(null=True, blank=True, default=None)
    duration = models.IntegerField(null=True, blank=True, default=None)
    billsec = models.IntegerField(null=True, blank=True, default=None)
    hangup_cause = models.CharField(max_length=80, null=True, blank=True, default=None)
    uuid = models.CharField(max_length=120, blank=True, default=None, primary_key=True)
    bleg_uuid = models.CharField(max_length=120, null=True, blank=True, default=None)
    accountcode = models.CharField(max_length=80, null=True, blank=True, default=None)
    company = models.CharField(max_length=80, null=True, blank=True, default=None)

    class Meta:
        db_table = 'fs_cdr'


class FsUser(models.Model):
    userid = models.CharField(max_length=30, null=True, blank=True, default=None)
    password = models.CharField(max_length=30, null=True, blank=True, default=None)
    accountcode = models.CharField(max_length=30, null=True, blank=True, default=None)
    user_context = models.CharField(max_length=20, null=True, blank=True, default=None)
    effective_caller_id_name = models.CharField(max_length=30, null=True, blank=True, default=None)
    effective_caller_id_number = models.CharField(max_length=20, null=True, blank=True, default=None)
    callgroup = models.CharField(max_length=10, null=True, blank=True, default=None)
    max_calls = models.IntegerField(max_length=2, null=True, blank=True, default=None)

    class Meta:
        db_table = 'fs_users'


class FsTier(models.Model):
    queue = models.CharField(max_length=255, null=True, blank=True, default=None)
    agent = models.CharField(max_length=255, null=True, blank=True, default=None)
    state = models.CharField(max_length=255, null=True, blank=True, default=None)
    level = models.IntegerField(default=1)
    position = models.IntegerField(default=1)

    class Meta:
        db_table = 'fs_tiers'


class FsAgent(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, default=None)
    system = models.CharField(max_length=255, null=True, blank=True, default=None)
    uuid = models.CharField(max_length=255, null=True, blank=True, default=None)
    type = models.CharField(max_length=255, null=True, blank=True, default=None)
    contact = models.CharField(max_length=255, null=True, blank=True, default=None)
    status = models.CharField(max_length=255, null=True, blank=True, default=None)
    state = models.CharField(max_length=255, null=True, blank=True, default=None)
    max_no_answer = models.IntegerField(default=0)
    wrap_up_time = models.IntegerField(default=0)
    reject_delay_time = models.IntegerField(default=0)
    busy_delay_time = models.IntegerField(default=0)
    no_answer_delay_time = models.IntegerField(default=0)
    last_bridge_start = models.IntegerField(default=0)
    last_bridge_end = models.IntegerField(default=0)
    last_offered_call = models.IntegerField(default=0)
    last_status_change = models.IntegerField(default=0)
    no_answer_count = models.IntegerField(default=0)
    calls_answered = models.IntegerField(default=0)
    talk_time = models.IntegerField(default=0)
    ready_time = models.IntegerField(default=0)

    class Meta:
        db_table = 'fs_agents'
