from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        identifier = request.POST['identifier']
        password = request.POST['password']

        # Check if the identifier is an email or a username
        try:
            user = User.objects.get(Q(username=identifier) | Q(email=identifier))
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')


@login_required(login_url='login')
def item_list_view(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create(username=username, first_name=first_name, last_name=last_name,
                                   email=email)
        user.set_password(password)
        user.save()
        user = authenticate(request, username=username, password=password)

        # Log in the user
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return render(request, 'register.html', {'error': 'Registration successful but unable to log in.'})
    else:
        return render(request, 'register.html')
    return render(request, 'register.html')

# Create your views here.
