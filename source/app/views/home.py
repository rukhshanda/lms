from django.shortcuts import render


def index(request):
    return render(
        request,
        'home/index.html',
        {}
    )


def profile(request):
    raise NotImplementedError('This view is not implemented yet.')


def support(request):
    raise NotImplementedError('This view is not implemented yet.')
