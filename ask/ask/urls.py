from django.conf.urls import include, url, patterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
url(r'^', include('ask.urls')),
url(r'^admin/', include('admin.site.urls')),
]
