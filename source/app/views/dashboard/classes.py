from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required

from app.models.classes import Class
from app.forms.classes import ClassForm


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
