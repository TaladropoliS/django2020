from django.shortcuts import render, HttpResponse


def prueba(request):
    return render(request, 'index.html')
