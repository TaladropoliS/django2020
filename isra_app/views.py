<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
=======
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def index(request):
    return HttpResponse('hola')

>>>>>>> daa260eb2d3df252f6c93a6417e34cae72d69a31
# Create your views here.
def index(request):
    return render(request, 'index.html')

def inicio(request):
    errors = User.objects.validacion(request.POST)
    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/')
    return render(request, 'home.html')