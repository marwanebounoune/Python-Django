from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import ListClients


def index(request):
    print("hello 0")
    return render(request, 'pages/index.html')

def formul(request):
    print("hello 4")
    return render(request, 'pages/form.html')


def postClient(request):
    if request.method == 'POST':
        nom1= request.POST['nom']
        prenom1= request.POST['prenom']
        enregistrement= ListClients(nom=nom1, prenom=prenom1)
        enregistrement.save()
        print("hello1")
        return HttpResponseRedirect('clients/succes')


def failed(request):
    return render(request, 'pages/failed.html')

def succes(request):
    cli = ListClients.objects.all()
    context = {
        'clients': cli
    }
    return render(request, 'pages/succes.html', context)