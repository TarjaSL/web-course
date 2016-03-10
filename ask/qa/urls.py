from django.conf.urls import include, url
from qa.views import test

urlpatterns = [
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', test, name='index'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', est, name='signup'),
    url(r'^question/(?P<id>[0-9]+)/$', test, name='question'),
    url(r'^ask/', test, name='ask'),
    url(r'^popular/', test, name='popular'),
    url(r'^new/', test, name='new'),
    
]


