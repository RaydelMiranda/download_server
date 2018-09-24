#! -*- coding: utf-8 -*-
from django.conf.urls import url

from download.views import NewDownloadView, RemoveDownload, UpdateDownload, \
    ResumeDownload

urlpatterns = [
    url(r'new_download', NewDownloadView.as_view(), name='new_download'),
    url(r'remove_download', RemoveDownload.as_view(), name='remove_download'),
    url(r'update_download', UpdateDownload.as_view(), name='update_download'),
    url(r'pause_download', UpdateDownload.as_view(), name='pause_download'),
    url(r'resume_download', ResumeDownload.as_view(), name='resume_download'),
    url(r'cancel_download', ResumeDownload.as_view(), name='cancel_download'),
    url(r'download_list', ResumeDownload.as_view(), name='download_list'),
    url(r'download_detail', ResumeDownload.as_view(), name='download_detail'),
]
