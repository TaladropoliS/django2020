from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('hola')

# Create your views here.
def palma(request):
    errors = User.objects.validacion(request.POST)
    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/')
    return redirect('israel/')