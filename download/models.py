# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.utils.translation import ugettext as _


class FileMetaData(models.Model):
    size = models.DecimalField(_("Size of the file"), decimal_places=2,
                               max_digits=10)
    type = models.CharField(_("File type"), max_length=255)


class DownloadTask(models.Model):
    url = models.URLField(_("Target url"), db_index=True)
    file_path = models.FilePathField(
        _("File path"), null=True, blank=True, db_index=True
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=SET_NULL
    )

    duration = models.DurationField(
        _("Duration"), max_length=255,
        default=timedelta(hours=0, minutes=0, seconds=0)
    )

    progress = models.IntegerField(_("Progress"), default=0)
    start_time = models.DateTimeField(_("Init time"), blank=False, null=True)

    auto_pause = models.BooleanField(
        _("Set pause automatically"),
        default=False
    )

    auto_pause_time = models.TimeField(
        _("Pause download at this time"),
        null=True, blank=True
    )

    auto_resume_time = models.TimeField(
        _("Resume download at this time"),
        null=True, blank=True
    )

    TASK_STATUS_STARTED = 0
    TASK_STATUS_PAUSED = 1
    TASK_STATUS_CANCELED = 2
    TASK_STATUS_DELETED = 3
    TASK_STATUS_COMPLETED = 4
    TASK_STATUS_ON_HOLD = 5

    TASK_STATUS_OPTIONS = (
        (TASK_STATUS_STARTED, _("Started")),
        (TASK_STATUS_PAUSED, _("Paused")),
        (TASK_STATUS_CANCELED, _("Canceled")),
        (TASK_STATUS_DELETED, _("Deleted")),
        (TASK_STATUS_COMPLETED, _("Completed")),
        (TASK_STATUS_ON_HOLD, _("On hold"))
    )

    status = models.IntegerField(_("Status"), choices=TASK_STATUS_OPTIONS,
                                 default=TASK_STATUS_ON_HOLD)

    TASK_PRIORITY_HIGH = 1
    TASK_PRIORITY_MEDIUM = 2
    TASK_PRIORITY_LOW = 3

    TASK_PRIORITY_OPTIONS = (
        (TASK_PRIORITY_HIGH, _("High priority")),
        (TASK_PRIORITY_MEDIUM, _("Medium priority")),
        (TASK_PRIORITY_LOW, _("Low priority"))
    )

    priority = models.IntegerField(_("Priority"), choices=TASK_PRIORITY_OPTIONS,
                                   default=TASK_PRIORITY_MEDIUM)

    TASK_SCOPE_PRIVATE = 1
    TASK_SCOPE_PUBLIC = 2

    TASK_SCOPE_CHOICES = (
        (TASK_SCOPE_PRIVATE, _("Private")),
        (TASK_SCOPE_PUBLIC, _("Public")),
    )

    scope = models.IntegerField(_("Scope"), choices=TASK_SCOPE_CHOICES,
                                default=TASK_SCOPE_PUBLIC)

    file_metadata = models.ForeignKey(FileMetaData, on_delete=SET_NULL,
                                      null=True)

    def __str__(self):
        return self.url
