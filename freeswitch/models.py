# coding=utf-8

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core import urlresolvers
import datetime

class Cdr(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    caller_id_name = models.CharField(max_length=50, null=True, blank=True, default=None)
    caller_id_number = models.CharField(max_length=50, null=True, blank=True, default=None)
    destination_number = models.CharField(max_length=50, null=True, blank=True, default=None)
    context = models.CharField(max_length=80, null=True, blank=True, default=None)
    start_stamp = models.DateTimeField()
    answer_stamp = models.DateTimeField()
    end_stamp = models.DateTimeField()
    duration = models.IntegerField()
    billsec = models.IntegerField()
    hangup_cause = models.CharField(max_length=80, null=True, blank=True, default=None)
    uuid = models.CharField(max_length=120, null=True, blank=True, default=None)
    bleg_uuid = models.CharField(max_length=120, null=True, blank=True, default=None)
    accountcode = models.CharField(max_length=80, null=True, blank=True, default=None)
    company = models.CharField(max_length=80, null=True, blank=True, default=None)

    class Meta:
        db_table = 'fs_cdr'
