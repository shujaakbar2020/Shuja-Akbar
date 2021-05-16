from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'Resume/base.html', {})


def first(request):
    return render(request, 'Resume/test.html', {})
