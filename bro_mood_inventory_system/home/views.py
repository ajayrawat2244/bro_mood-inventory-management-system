from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.hashers import make_password

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
        username = request.POST.get("email")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        userrole = request.POST.get("userrole")
        password = request.POST.get("password")
        parentuser = request.user
        email = email.lower()
        cus = User.objects.filter(Q(email=email) | Q(username=username))
        if cus:
            return HttpResponse("username or email already exists")
        else:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.is_active = True
            user.save()
            parent_profile = UserProfile.objects.get(user=parentuser)
            parent_company = parent_profile.company
            profileinfo = UserProfile(user=user, mobile=mobile, userrole=userrole,
                                      parentuser=parentuser, company=parent_company)
            profileinfo.save()
            return redirect('/add-company')
    else:
        return render(request, 'register.html')

def add_company(request):
    options = UserProfile.objects.filter(userrole='superadmin')
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        domain = request.POST.get("domain")
        created_by_username = request.POST.get("created_by")
        created_by_user = User.objects.get(username=created_by_username)
        created_by_id = int(created_by_user.id)
        created_by = User.objects.get(id=created_by_id)
        state = request.POST.get("state")
        district = request.POST.get("district")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        company = Company.objects.create(name=name, phone=phone, domain=domain, created_by=created_by)
        company.save()
        company_address = Company_address.objects.create(state=state, district=district, city=city,
                                                         pincode=pincode, company=company)
        company_address.save()
        superuser_profile = UserProfile.objects.get(user=created_by)
        superuser_profile.company = company
        superuser_profile.save()
        return redirect('/')
    return render(request, 'add_company.html', {'options': options})


"""@login_required(login_url='login')
def add_subuser(request):
    if request.method == "POST":
        name = request.POST.get("name")
        userid = request.POST.get("userid")
        password = request.POST.get("password")
        role = request.POST.get("role")
        company = request.user
        subuser = Subuser.objects.create(name=name, userid=userid, password=make_password(password),
                                         role=role, company=company)
        subuser.save()
        return redirect('/subuser-list')
    return render(request, 'add_subuser.html')

@login_required(login_url='login')
def subuser_list(request):
    records_per_page = 10
    company = request.user
    subuser_list = Subuser.objects.filter(company=company)
    paginator = Paginator(subuser_list, records_per_page)
    page_number = request.GET.get('page')
    total_page = paginator.num_pages
    records_for_page = paginator.get_page(page_number)
    total_page_list = [n + 1 for n in range(total_page)]
    data = {
        'subuser_list': records_for_page, "num_pages": total_page,
        "total_page_list": total_page_list, "page_number": page_number,
    }
    return render(request, 'subuser_list.html', data)"""


