from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calc/', views.calcStatus, name='calc'),
    path('chart/', views.chart, name='report' ),
    path('alert/', views.alert, name='alert'),
    path('chart/getdata/', views.getData, name='getdata'),
]