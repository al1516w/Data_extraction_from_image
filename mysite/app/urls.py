from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.uploadimage, name='uploadimage'),
    path('view_uploads', views.view_uploads, name='view_uploads'),
]