from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    return render(request, 'index.html')

def inicio(request):
    errors = User.objects.validacion(request.POST)
    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/')
    request.session['usuario'] = request.POST['nombre']
    context = {
        "usuario":request.POST['nombre'],
        "diccionario" : {"nombre": request.POST['nombre'], "Email": request.POST['email']}
    }
    return render(request, 'home.html',context)