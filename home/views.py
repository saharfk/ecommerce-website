from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from .models import Comments


# Create your views here.
def index(request):
    allComments = Comments.objects.all()

    context = {'allComments': allComments}

    return render(request, 'index.html', context)
