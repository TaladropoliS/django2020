from django.shortcuts import render, redirect, HttpResponse
# import random
from random import randrange
# Create your views here.

def tala(request):
    return render(request, 'index1.html')
