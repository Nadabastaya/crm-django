from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home')

def costumer(request):
    return HttpResponse('Costumer')

def products(request):
    return HttpResponse('Products')