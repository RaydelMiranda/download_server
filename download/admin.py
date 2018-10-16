# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin

from download.models import DownloadTask


class AdminDownloadTask(admin.ModelAdmin):
    list_display = ('url', 'owner', 'status')
    list_filter = ['owner', 'status']


admin.site.register(DownloadTask, AdminDownloadTask)
