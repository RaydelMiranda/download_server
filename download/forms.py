#! -*- coding: utf-8 -*-
from django import forms

from download.models import DownloadTask


class NewDownloadTaskForm(forms.ModelForm):
    class Meta:
        model = DownloadTask
        fields = ['url', 'start_time', 'auto_pause', 'auto_pause_time',
                  'auto_resume_time', 'priority']
