from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from source.app.models.faculty import Teacher
from source.app.models.classes import Class


@login_required(redirect_field_name=None)
def index(request):
    return render(
        request,
        'dashboard/index.html',
        {}
    )


@login_required(redirect_field_name=None)
def teacher(request):
    teachers = Teacher.objects.all().order_by('first_name', 'last_name')

    return render(
        request,
        'dashboard/teacher.html',
        {
            'teachers': teachers,
        }
    )


@login_required(redirect_field_name=None)
def _class(request):
    classes = Class.objects.all().order_by('-year')

    return render(
        request,
        'dashboard/class.html',
        {
            'classes': classes,
        }
    )
