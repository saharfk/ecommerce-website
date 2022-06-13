from django.urls import path

from . import views

urlpatterns = [
    path('', views.service, name='service'),
    path('template/', views.template, name='template'),
    path('sample/', views.sample, name='sample'),
    # adding some thing
    #     path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    #     path('colors/', views.colors, name='colors'),
]
