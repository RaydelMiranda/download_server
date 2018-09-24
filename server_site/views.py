# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'server_site/home.html'
