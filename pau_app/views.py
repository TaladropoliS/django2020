from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("Holi")

def saludo(request):
    return HttpResponse('Holi')

# Create your views here.
def index(request):
    pass