"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django import urls
from django.urls import path, include

urlpatterns = [
    path('cristian/', include('cristian_app.urls')),
    path("andres/", include('toro_app.urls')),
    path('', include('isra_app.urls')),
    path('camila/', include('camila_riquelme.urls')),
    path('carlos/', include('carlos_app.urls')),
    path('nueva_app1', include('nueva_app001.urls')),
    path('diego_esparza', include('diego_esparza.urls')),
    path('jalvarez/', include('jalvarez.urls')),
    path('diego_labrin/', include('diego_labrin.urls')),
    path('paula/', include('pau_app.urls')),
    path('fernando/', include('taladropolis.urls')),
]
