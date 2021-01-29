<<<<<<< HEAD
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('hola')

=======
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
>>>>>>> e72cdbaa4156bff28ff210185858df6f9206200c
# Create your views here.
def palma(request):
    errors = User.objects.validacion(request.POST)
    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/')
    return redirect('israel/')