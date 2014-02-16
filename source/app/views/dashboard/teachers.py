from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required

from app.models.faculty import Teacher
from app.forms.faculty import TeacherForm


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

    teacher.deleted = True
    teacher.save()

    return redirect('/dashboard/teacher/')
