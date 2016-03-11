from django.conf.urls import include, url

from qa.views import test
urlpatterns = patterns('qa.views',
url(r'^$', test),
)
