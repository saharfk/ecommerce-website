from django.shortcuts import render


# Create your views here.
def service(request):
    return render(request, 'servicesS.html')


def sample(request):
    return render(request, 'Sample.html')


def info(request):
    return render(request, 'productInfoS.html')
