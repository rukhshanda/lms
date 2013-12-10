from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required

from source.app.models.faculty import Teacher
from source.app.models.classes import Class
from source.app.models.groups import Group
from source.app.forms.faculty import TeacherForm
from source.app.forms.classes import ClassForm


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
def teacher_add(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/teacher/')
    else:
        form = TeacherForm()

    return render(
        request,
        'dashboard/teacher_edit.html',
        {
            'form': form,
        }
    )


@login_required(redirect_field_name=None)
def teacher_edit(request, id):
    try:
        teacher = Teacher.objects.get(pk=id)
    except Teacher.DoesNotExist:
        return Http404

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/teacher/')
    else:
        form = TeacherForm(instance=teacher)

    return render(
        request,
        'dashboard/teacher_edit.html',
        {
            'form': form,
        }
    )


@login_required(redirect_field_name=None)
def teacher_delete(request, id):
    try:
        teacher = Teacher.objects.get(pk=id)
    except Teacher.DoesNotExist:
        return Http404

    teacher.is_active = False
    teacher.save()

    return redirect('/dashboard/teacher/')


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


@login_required(redirect_field_name=None)
def class_add(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/class/')
    else:
        form = ClassForm()

    return render(
        request,
        'dashboard/class_edit.html',
        {
            'form': form,
        }
    )


@login_required(redirect_field_name=None)
def class_edit(request, id):
    try:
        cls = Class.objects.get(pk=id)
    except Class.DoesNotExist:
        return Http404

    if request.method == 'POST':
        form = ClassForm(request.POST, instance=cls)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/class/')
    else:
        form = ClassForm(instance=cls)

    return render(
        request,
        'dashboard/class_edit.html',
        {
            'form': form,
        }
    )


@login_required(redirect_field_name=None)
def group(request):
    groups = Group.objects.all().order_by('name', 'cclass__year')

    return render(
        request,
        'dashboard/group.html',
        {
            'groups': groups,
        }
    )
