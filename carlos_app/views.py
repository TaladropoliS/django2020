from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def app(request):
    return HttpResponse("XD")
# Create your views here.
