from django.conf.urls import include, url, patterns

from qa.views import test
urlpatterns = patterns('qa.views',
url(r'^$', test),
)
