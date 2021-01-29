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
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
    #    path('admin/', admin.site.urls),
    path('blog/', include('camila_riquelme.urls')),
    path('carlos/', include('carlos_app.urls')),
    path('isra/', include('isra_app.urls')),

=======

>>>>>>> c7ff8b96a049afaf2072640cfd77be020c3081f6
    #    path('admin/', admin.site.urls),
    path('blog/', include('camila_riquelme.urls')),
    #path('admin/', admin.site.urls),
    path('blog/', include('isra_app.urls')),
    path('gtoro/', include('toro_app.urls')),
    path('blog/', include('blog.urls')),
    path('nueva_app1', include('nueva_app001.urls')),
    path('diego_esparza', include('diego_esparza.urls')),
    path('blog/', include('camila_riquelme.urls')),
    path('blog/', include('blog.urls'))
<<<<<<< HEAD
=======
>>>>>>> c9a283ea276a7556ad37dbe89a610a271e632e8c
>>>>>>> 0ec41b098973e7f632b13db9f0e103f2bfb9c141
=======
    path('blog/', include('camila_riquelme.urls')),
    path('nueva_app1', include('nueva_app001.urls')),
    path('diego_esparza', include('diego_esparza.urls'))
>>>>>>> e72cdbaa4156bff28ff210185858df6f9206200c
>>>>>>> c7ff8b96a049afaf2072640cfd77be020c3081f6
]
