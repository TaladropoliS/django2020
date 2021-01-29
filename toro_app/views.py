from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    HttpResponse('He ingresado a la app')