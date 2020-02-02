from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index),
    path('history/', views.history),
    path('api/v1/cities/<str:symbol>', views.cities)
]