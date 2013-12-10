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
    url(r'^dashboard/teacher/$', dashboard.teacher, name='dashboard.teacher'),
    url(r'^dashboard/teacher/add/$', dashboard.teacher_add, name='dashboard.teacher_add'),
    url(r'^dashboard/teacher/(?P<id>\d+)/$', dashboard.teacher_edit, name='dashboard.teacher_edit'),
    url(r'^dashboard/teacher/(?P<id>\d+)/delete/$', dashboard.teacher_delete, name='dashboard.teacher_delete'),
    url(r'^dashboard/class/$', dashboard._class, name='dashboard.class'),
    url(r'^dashboard/class/add/$', dashboard.class_add, name='dashboard.class_add'),
    url(r'^dashboard/class/(?P<id>\d+)/$', dashboard.class_edit, name='dashboard.class_edit'),
    url(r'^dashboard/group/$', dashboard.group, name='dashboard.group'),

)
