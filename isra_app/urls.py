<<<<<<< HEAD
from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	   
=======
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('inicio', views.inicio)
>>>>>>> 60fd8c8dd510c7410b44064cc6b487bd2f08c1cd
]