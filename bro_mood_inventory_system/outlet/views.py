# views.py
from django.shortcuts import render, HttpResponse

def item_list_view(request):
    return render(request, 'index.html')

def list(request):
    return HttpResponse("you can see the outlet list very shortly")
def add_outlet(request):
    return render(request,'outlet/add_outlet.html')


# Create your views here.
