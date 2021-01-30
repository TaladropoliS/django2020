<<<<<<< HEAD
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('hola')

=======
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
>>>>>>> 60fd8c8dd510c7410b44064cc6b487bd2f08c1cd
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
        "usuario":request.POST['nombre']
    }
    return render(request, 'home.html',context)