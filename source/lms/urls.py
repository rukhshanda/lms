from django.conf.urls import patterns, include, url
from django.contrib import admin

from source.app.views import home, auth, dashboard

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Auth URLs
    url(r'^auth/signin/$', auth.signin, name='auth.signin'),
    url(r'^auth/signout/$', auth.signout, name='auth.signout'),
    url(r'^auth/forgot_password/$', auth.forgot_password, name='auth.forgot_password'),

    # Home URLs
    url(r'^$', home.index, name='home.index'),
    url(r'^profile/$', home.profile, name='home.profile'),
    url(r'^support/$', home.support, name='home.support'),

    # Dashboard URLs
    url(r'^dashboard/$', dashboard.index, name='dashboard.index'),
)
