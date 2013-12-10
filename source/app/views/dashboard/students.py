from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required

from source.app.models.students import Student
from source.app.forms.students import StudentForm


@login_required(redirect_field_name=None)
def student(request):
    students = Student.objects.all().order_by('first_name', 'last_name')

    return render(
        request,
        'dashboard/student.html',
        {
            'students': students,
        }
    )


@login_required(redirect_field_name=None)
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/student/')
    else:
        form = StudentForm()

    return render(
        request,
        'dashboard/student_edit.html',
        {
            'form': form,
        }
    )


@login_required(redirect_field_name=None)
def student_edit(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Http404

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/student/')
    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'dashboard/student_edit.html',
        {
            'form': form,
        }
    )


@login_required(redirect_field_name=None)
def student_delete(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Http404

    student.is_active = False
    student.save()

    return redirect('/dashboard/student/')
