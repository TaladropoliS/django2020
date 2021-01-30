from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def new (request):
    return render(request, 'create.html')

def create (request):
    errors = Tv.objects.validations(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            print(key, '=',val)
            messages.error(request, val)
        return redirect('/diego_labrin/new/')

    else:
        Tv.objects.create(title=request.POST['title'], network=request.POST['net'],
        date=request.POST['date'], desc=request.POST['desc'])

        print('post de date:',request.POST['date'])
        id = Tv.objects.last().id
        return redirect(f'/diego_labrin/{id}')

def show_one (request, num):
    context = {
        'tv': Tv.objects.get(id=num)
    }
    return render(request, 'show_one.html', context)

def shows_all (request):
    context = {
        'tv': Tv.objects.all()
    }
    return render(request, 'show_all.html', context)

def edit (request, num):
    context = {
        'tv': Tv.objects.get(id=num)
    }
    return render(request, 'update.html', context)

def update (request, num):
    objeto = Tv.objects.get(id=num)
    objeto.title = request.POST['title']
    objeto.network = request.POST['net']
    objeto.date = request.POST['date']
    objeto.desc = request.POST['desc']
    objeto.save()
    print('post de date:', request.POST['date'])
    print('date obj:', objeto.date.replace('-','/'))
    return redirect(f'/diego_labrin/{num}')

def destroy (request, num):
    objecto=Tv.objects.get(id=num)
    objecto.delete()
    return redirect('/')