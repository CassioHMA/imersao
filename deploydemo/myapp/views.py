from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, amiguinhos imersão 2")

# Create your views here.
