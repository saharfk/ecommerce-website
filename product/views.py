from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def service(request):
    return render(request, 'services.html')


def template(request):
    return render(request, 'templateSample.html')


def sample(request):
    return render(request, 'templateSample.html')


def info(request):
    return render(request, 'productInfo.html')
