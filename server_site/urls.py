from django.conf.urls import url

from server_site.views import Home

urlpatterns = [
    url('^$', Home.as_view(), name='home')
]
