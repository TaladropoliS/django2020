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
>>>>>>> c81ed23489ac4f0a374ee9386d765bcf4281844a
    path('', include('isra_app.urls')),
    path('camila/', include('camila_riquelme.urls')),
    path('tala', include('taladropolis.urls')),
    path('blog/', include('camila_riquelme.urls')),
    path('carlos/', include('carlos_app.urls')),
    path('nueva_app1', include('nueva_app001.urls')),
    path('diego_esparza', include('diego_esparza.urls')),
<<<<<<< HEAD
    path('jalvarez/', include('jalvarez.urls')),
    path('', include('cristian_app.urls')),

#     #    path('admin/', admin.site.urls),
# <<<<<<< HEAD
#     path('blog/', include('camila_riquelme.urls'))
# =======
#     #path('admin/', admin.site.urls),
#     path('blog/', include('blog.urls')),
#     path('nueva_app1', include('nueva_app001.urls')
# >>>>>>> 257762343cb13630f74bd3825691968193246bab
# =======
#     path('diego_esparza', include('diego_esparza.urls')),
#     path('blog/', include('camila_riquelme.urls')),
#     path('blog/', include('blog.urls'))
# >>>>>>> c9a283ea276a7556ad37dbe89a610a271e632e8c

=======
    path('diego_labrin/', include('diego_labrin.urls')),
    path('', include('cristian_app.urls')),
>>>>>>> c81ed23489ac4f0a374ee9386d765bcf4281844a
]
