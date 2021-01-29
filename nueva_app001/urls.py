from django.urls import path
from . import views

urlpatterns = [
    path('', views.nueva_app1)
]