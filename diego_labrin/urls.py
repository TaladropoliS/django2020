from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows_all),
    path('new/', views.new, name='new'),
    path('create/', views.create),
    path('<int:num>/', views.show_one, name='show_one'),
    path('<int:num>/edit/', views.edit, name='edit'),
    path('<int:num>/update/', views.update, name='update'),
    path('<int:num>/destroy/', views.destroy, name='destroy'),
]