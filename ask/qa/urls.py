from django.conf.urls import include, url, patterns

urlpatterns = patterns('qa.views',
   url(r'^$', 'test'),
   url(r'^login/', 'test'),
   url(r'^signup/', 'test'),
   url(r'^question/(?P<id>[0-9]+)/$'),
   url(r'^ask/', 'test'),
   url(r'^popular/', 'test'),   
   url(r'^new/', 'test'),  
)

