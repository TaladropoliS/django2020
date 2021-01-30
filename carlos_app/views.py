from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "carlos_index.html")

# Create your views here.
