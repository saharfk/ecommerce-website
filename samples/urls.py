from django.urls import path

from . import views

urlpatterns = [
    path('', views.service, name='serviceS'),
    path('samples/', views.sample, name='samples'),
    path('info/', views.info, name='infoS'),
    # adding some thing
    #     path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    #     path('colors/', views.colors, name='colors'),
]
