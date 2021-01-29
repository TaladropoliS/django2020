from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def palma(request):
    errors = User.objects.validacion(request.POST)
    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/')
    return redirect('israel/')