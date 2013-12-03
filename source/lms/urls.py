from django.conf.urls import patterns, include, url
from django.contrib import admin

from source.app.views import home

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Home URLs
    url(r'^$', home.index, name='home.index'),
)
