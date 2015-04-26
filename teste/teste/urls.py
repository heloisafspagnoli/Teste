from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from CoinDeterminer.views import upload_file
 
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', upload_file, name="home"),
)
