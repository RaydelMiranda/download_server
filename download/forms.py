#! -*- coding: utf-8 -*-
from django import forms

from download.models import DownloadTask


class NewDownloadForm(forms.ModelForm):
    class Meta:
        model = DownloadTask
        fields = ['url', 'owner', 'auto_pause', 'auto_pause_time',
                  'auto_resume_time', 'priority']
