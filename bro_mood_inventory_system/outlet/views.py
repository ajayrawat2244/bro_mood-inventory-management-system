# views.py
from django.shortcuts import render

def item_list_view(request):
    return render(request, 'index.html')


# Create your views here.
