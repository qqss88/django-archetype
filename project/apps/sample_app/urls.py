from django.conf.urls.defaults import *
import dselector

from archetype import views

parser = dselector.Parser()
url = parser.url


urlpatterns = parser.patterns('',
    url(r'', views.home, name='home'),
)
