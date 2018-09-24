#! -*- coding: utf-8 -*-
import datetime

import pytest
from dateutil.relativedelta import relativedelta
from django.urls import reverse, NoReverseMatch

# -----------------------------------------------------------------------------
# Tests for views.
# -----------------------------------------------------------------------------
from download.models import DownloadTask


class TestForViews(object):
    download_urls_names = [
        'new_download', 'remove_download', 'update_download',
        'pause_download', 'resume_download', 'cancel_download',
        'download_list', 'download_detail',
    ]

    @pytest.mark.parametrize('view_name', download_urls_names)
    def test_download_urls(self, view_name):
        try:
            reverse(view_name)
        except NoReverseMatch:
            assert False, "No url defined for: {}".format(view_name)

    def test_download_creation(self, db, client, test_user):  # noqa

        # Create the download.
        dummy_url = 'http://dummy_url.dummy'
        data = {
            'url': dummy_url,
            'owner': test_user,
            'start_time': datetime.datetime.now(),
            'auto_pause': True,
            'auto_pause_time': datetime.datetime.now() + relativedelta(hours=2),
            'auto_resume_time': datetime.datetime.now() + relativedelta(hours=4)
        }
        client.post(reverse('new_download'), data)

        # Check for the download creation.
        download = DownloadTask.objects.get(url=dummy_url)
