from django.conf.urls import include, url, patterns
from django.contrib import admin
admin.autodiscover()
from ask.views import test

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    url(r'^', include('qa.urls')),
    url(r'^admin/', include('admin.site.urls')),
)
