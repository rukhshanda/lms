from django.shortcuts import render


def index(request):
    return render(
        request,
        'base.html',
        {}
    )


def profile(request):
    raise NotImplementedError('This view is not implemented yet.')


def dashboard(request):
    raise NotImplementedError('This view is not implemented yet.')
