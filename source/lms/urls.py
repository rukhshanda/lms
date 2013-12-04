from django.conf.urls import patterns, include, url
from django.contrib import admin

from source.app.views import home, auth

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Home URLs
    url(r'^$', home.index, name='home.index'),
    url(r'^profile/$', home.profile, name='home.profile'),
    url(r'^dashboard/$', home.dashboard, name='home.dashboard'),

    # Auth URLs
    url(r'^auth/signin/$', auth.signin, name='auth.signin'),
    url(r'^auth/signout/$', auth.signout, name='auth.signout'),
    url(r'^auth/forgot_password/$', auth.forgot_password, name='auth.forgot_password'),
)
