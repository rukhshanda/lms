from django.conf.urls import patterns, include, url
from django.contrib import admin

from app.views import home, auth
from app.views.dashboard import home as dashboard, teachers, classes, students, groups

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
    url(r'^dashboard/teacher/$', teachers.teacher, name='dashboard.teacher'),
    url(r'^dashboard/teacher/add/$', teachers.teacher_add, name='dashboard.teacher_add'),
    url(r'^dashboard/teacher/(?P<id>\d+)/$', teachers.teacher_edit, name='dashboard.teacher_edit'),
    url(r'^dashboard/teacher/(?P<id>\d+)/delete/$', teachers.teacher_delete, name='dashboard.teacher_delete'),
    url(r'^dashboard/class/$', classes._class, name='dashboard.class'),
    url(r'^dashboard/class/add/$', classes.class_add, name='dashboard.class_add'),
    url(r'^dashboard/class/(?P<id>\d+)/$', classes.class_edit, name='dashboard.class_edit'),
    url(r'^dashboard/group/$', groups.group, name='dashboard.group'),
    url(r'^dashboard/group/add/$', groups.group_add, name='dashboard.group_add'),
    url(r'^dashboard/group/(?P<id>\d+)/$', groups.group_edit, name='dashboard.group_edit'),
    url(r'^dashboard/student/$', students.student, name='dashboard.student'),
    url(r'^dashboard/student/add/$', students.student_add, name='dashboard.student_add'),
    url(r'^dashboard/student/(?P<id>\d+)/$', students.student_edit, name='dashboard.student_edit'),
    url(r'^dashboard/student/(?P<id>\d+)/delete/$', students.student_delete, name='dashboard.student_delete'),
    url(r'^dashboard/student/import/$', students.student_import, name='dashboard.student_import'),
)
