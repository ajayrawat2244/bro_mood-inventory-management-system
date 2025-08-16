# views.py
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from home.models import UserProfile, Company
from product.models import *
from django.db.models import Q
from decimal import Decimal
from .forms import JournalFilterForm


@login_required(login_url='login')
def item_list_view(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def add_outlet(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        state = request.POST.get("state")
        district = request.POST.get("district")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        contact_information = request.POST.get("contact_information")
        user = request.user
        #userprofile = UserProfile.objects.get(user=user)
        #company = userprofile.company
        outlet = Outlet(name=name, state=state, district=district, city=city, pincode=pincode,
                        contact_information=contact_information, user=user)#company=company
        outlet.save()
        return redirect('/outlet/list')
    return render(request, 'outlet/add_outlet.html')

@login_required(login_url='login')
def outlet_list(request):
    records_per_page = 10
    user = request.user
    outlet_list = Outlet.objects.filter(user=user)
    paginator = Paginator(outlet_list, records_per_page)
    page_number = request.GET.get('page')
    total_page = paginator.num_pages
    records_for_page = paginator.get_page(page_number)
    total_page_list = [n + 1 for n in range(total_page)]
    data = {
        'outlet_list': records_for_page, "num_pages": total_page,
        "total_page_list": total_page_list, "page_number": page_number
    }
    return render(request, 'outlet/outlet_list.html', data)

@login_required(login_url='/login')
def add_journal(request):
    #article_list= Article.objects.all()
    if request.method == 'POST':
        product_list = request.POST.getlist('article[]')
        category_list = request.POST.getlist('category[]')
        size_list = request.POST.getlist('size[]')
        color_list = request.POST.getlist('color[]')
        debit_list = request.POST.getlist('debit[]')
        date_list = request.POST.getlist('date[]')
        quantity_list = request.POST.getlist('quantity[]')
        for article, category, size, color, debit, date, quantity in zip(product_list, category_list, size_list, color_list, debit_list, date_list, quantity_list):
            #article = Article.objects.get(id=int(articles))
            quantity= int(quantity)
            for _ in range(quantity):
                Journal.objects.create(
                    article=article,
                    category=category,
                    size=size,
                    color=color,
                    debit=debit,
                    register_date=date
                )
        return redirect('journal-list')
    return render(request, 'outlet/add_journal.html')

@login_required(login_url='/login')
def journal_list(request):
    journals = Journal.objects.all()

    selected_categories = request.GET.getlist("category")
    selected_articles = request.GET.getlist("article")
    selected_sizes = request.GET.getlist("size")
    selected_colors = request.GET.getlist("color")

    if selected_categories:
        journals = journals.filter(category__in=selected_categories)

    if selected_articles:
        journals = journals.filter(article__in=selected_articles)

    if selected_sizes:
        journals = journals.filter(size__in=selected_sizes)

    if selected_colors:
        journals = journals.filter(color__in=selected_colors)

    count = journals.count()
    credit_journal_list = journals.filter(credit__gt=0.00)
    invest_on_credit = sum(j.debit for j in credit_journal_list)
    sold_count = credit_journal_list.count()
    avl_count = count - sold_count
    total_debit = sum(journal.debit for journal in journals)
    total_credit = sum(journal.credit for journal in journals)

    data = {
        "journals": journals,
        "total_debit": total_debit,
        "total_credit": total_credit,
        "count": count,
        "invest_on_credit": invest_on_credit,
        "sold_count": sold_count,
        "avl_count": avl_count,
        "article_list": Journal.objects.values_list("article", flat=True).distinct(),
        "category_list": Journal.objects.values_list("category", flat=True).distinct(),
        "size_list": Journal.objects.values_list("size", flat=True).distinct(),
        "color_list": Journal.objects.values_list("color", flat=True).distinct(),
        "selected_articles": selected_articles,
        "selected_sizes": selected_sizes,
        "selected_colors": selected_colors,
    }

    return render(request, "outlet/journal_list.html", data)

""" #records_per_page = 10
    # user = request.user
    query = request.GET.get('q')
    if query:
        journal_list = Journal.objects.filter(
            Q(article=query) | Q(category=query),
            # user=user
        )
        count = journal_list.count()
        credit_journal_list = journal_list.filter(credit__gt=0.00)
        invest_on_credit = sum(credit_journal.debit for credit_journal in credit_journal_list)
        sold_count = credit_journal_list.count()
        avl_count = count - sold_count
        total_debit = sum(journal.debit for journal in journal_list)
        total_credit = sum(journal.credit for journal in journal_list)
    else:
        journal_list = Journal.objects.all()
        count = Journal.objects.count()
        credit_journal_list = journal_list.filter(credit__gt=0.00)
        invest_on_credit = sum(credit_journal.debit for credit_journal in credit_journal_list)
        sold_count = credit_journal_list.count()
        avl_count = count-sold_count
        total_debit = sum(journal.debit for journal in journal_list)
        total_credit = sum(journal.credit for journal in journal_list)
    #paginator = Paginator(journal_list, records_per_page)
    #page_number = request.GET.get('page')
    #total_page = paginator.num_pages
    #records_for_page = paginator.get_page(page_number)
    #total_page_list = [n + 1 for n in range(total_page)]
    if request.method == "POST":
        journal_id = request.POST.get("journal_id")  # Use the correct field name
        credit_value = request.POST.get("credit")
        credit_date = request.POST.get("date")

        if journal_id and credit_value:
            try:
                journal = Journal.objects.get(serial_no=journal_id)
                journal.credit += Decimal(credit_value)  # Update the credit value
                journal.credit_date = credit_date
                journal.save()
                return redirect('journal-list')  # Refresh the page after updating
            except Journal.DoesNotExist:
                pass
    data = {
        #'journal_list': records_for_page, "num_pages": total_page,
        #"total_page_list": total_page_list, "page_number": page_number,
        "journal_list": journal_list,
        'query': query, "total_debit": total_debit, "total_credit": total_credit, "count": count,
        "invest_on_credit": invest_on_credit, "sold_count": sold_count, "avl_count": avl_count
    }

    return render(request, 'outlet/journal_list.html', data)"""


@login_required(login_url='/login')
def add_stock(request):
    user = request.user
    #userprofile = UserProfile.objects.get(user=user)
    #company = userprofile.company
    outlet_list = Outlet.objects.all()#.filter(company=company)
    if request.method =='POST':
        product_list = request.POST.getlist('product[]')
        quantity_list = request.POST.getlist('quantity[]')
        unit_price_list = request.POST.getlist('unitPrice[]')
        customer_price_list = request.POST.getlist('customerPrice[]')
        reference_list = request.POST.getlist('reference[]')
        category_list = request.POST.getlist('category[]')
        outlet_id = int(request.POST.get('outlet'))
        outlet = Outlet.objects.get(id=outlet_id)
        date = request.POST.get('date')
        for product, quantity, unit_price, customer_price, reference, category in zip(product_list, quantity_list,
                                                                            unit_price_list, customer_price_list,
                                                                            reference_list, category_list):
            available_stock = AvailableStock(
                outlet=outlet,
                product=product,
                user=user,
                #company=company,
                category=category
            )
            available_stock.save()

            StockMovement.objects.create(
                product=available_stock,
                movement_type='IN',
                quantity=int(quantity),
                unit_price=float(unit_price),
                customer_price=float(customer_price),
                reference=reference,
                date=date,
                user=user,
                #company=company
            )
        return redirect('/outlet/list')
    return render(request, 'outlet/add_stock.html', {'outlet_list': outlet_list})

@login_required(login_url='/login')
def available_stock_list(request):
    records_per_page = 10
    user = request.user
    available_stock_list = AvailableStock.objects.filter(user=user)
    paginator = Paginator(available_stock_list, records_per_page)
    page_number = request.GET.get('page')
    total_page = paginator.num_pages
    records_for_page = paginator.get_page(page_number)
    total_page_list = [n + 1 for n in range(total_page)]
    data = {
        'available_stock_list': records_for_page, "num_pages": total_page,
        "total_page_list": total_page_list, "page_number": page_number
    }
    return render(request, 'outlet/available_stock_list.html', data)
# Create your views here.
