from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required

from app.models.groups import Group
from app.forms.groups import GroupForm


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


@login_required(redirect_field_name=None)
def group_add(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/group/')
    else:
        form = GroupForm()

    return render(
        request,
        'dashboard/group_edit.html',
        {
            'form': form,
        }
    )


@login_required(redirect_field_name=None)
def group_edit(request, id):
    try:
        group = Group.objects.get(pk=id)
    except Group.DoesNotExist:
        return Http404

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/group/')
    else:
        form = GroupForm(instance=group)

    return render(
        request,
        'dashboard/group_edit.html',
        {
            'form': form,
        }
    )
