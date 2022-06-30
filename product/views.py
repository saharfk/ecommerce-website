from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def service(request):
    return render(request, 'servicesP.html')


def template(request):
    return render(request, 'templateproduct.html')


def info(request):
    return render(request, 'productInfoP.html')
