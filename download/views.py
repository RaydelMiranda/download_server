# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, \
    DetailView

from download.forms import NewDownloadTaskForm
from download.models import DownloadTask


class NewDownloadView(CreateView):
    model = DownloadTask
    form_class = NewDownloadTaskForm
    template_name_suffix = '_new'


class CancelDownload(View):
    pass


class RemoveDownload(DeleteView):
    model = DownloadTask
    success_url = reverse_lazy('download_list')


class PauseDownloadView(View):
    pass


class UpdateDownload(UpdateView):
    model = DownloadTask


class ResumeDownload(View):
    pass


class DownloadList(ListView):
    model = DownloadTask


class DownloadDetail(DetailView):
    model = DownloadTask
