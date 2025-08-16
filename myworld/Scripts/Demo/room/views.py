from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html' )
    #return HttpResponse("welcome to the era of mr. Ajay")
def sections(request):
    return render(request, 'sections.html')
    #return HttpResponse("we are very excited to provide some
    # amazing sections very shortly")
def sale(request):
    return render(request, 'sale.html')
    #return HttpResponse("Top sales are coming very soon")

