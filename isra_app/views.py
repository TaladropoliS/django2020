from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('hola')

# Create your views here.
