# views.py
from django.shortcuts import render


def item_list_view(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

# Create your views here.
