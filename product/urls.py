from django.urls import path

from . import views

urlpatterns = [
    path('', views.service, name='serviceP'),
    path('template/', views.template, name='template'),
    path('info/', views.info, name='infoP'),
    # adding some thing
    #     path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    #     path('colors/', views.colors, name='colors'),
]
