from django.http import HttpResponse
from .models import Client
from django.shortcuts import render
from .models import Order, Product
from django.utils.timezone import now, timedelta

def client_orders(request, client_id):
    client_orders = Order.objects.filter(client_id=client_id)
    context = {'client_orders': client_orders}
    return render(request, 'client_detail.html', context)
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_detail(request, client_id):
    client = Client.objects.get(pk=client_id)
    return render(request, 'client_detail.html', {'client': client})

def client_products(request, client_id):
    client = Client.objects.get(pk=client_id)
    current_date = now()
    last_week_start = current_date - timedelta(days=7)
    last_month_start = current_date - timedelta(days=30)
    last_year_start = current_date - timedelta(days=365)

    last_week_orders = Order.objects.filter(client=client, order_date__gte=last_week_start, order_date__lt=current_date)
    last_month_orders = Order.objects.filter(client=client, order_date__gte=last_month_start,order_date__lt=current_date)
    last_year_orders = Order.objects.filter(client=client, order_date__gte=last_year_start, order_date__lt=current_date)

    last_week_products = list(set(Product.objects.filter(order__in=last_week_orders)))
    last_month_products = list(set(Product.objects.filter(order__in=last_month_orders)))
    last_year_products = list(set(Product.objects.filter(order__in=last_year_orders)))

    context = {
        'last_week_products': last_week_products,
        'last_month_products': last_month_products,
        'last_year_products': last_year_products,
    }

    return render(request, 'client_orders_list.html', context)
def home(request):
    html = """
    <html>
    <head>
        <title>Главная страница</title>
    </head>
    <body>
        <h1>Добро пожаловать на мой Django-сайт!</h1>
        <p>Это главная страница сайта.</p>
    </body>
    </html>
    """
    return HttpResponse(html)

def about(request):
    html = """
    <html>
    <head>
        <title>О себе</title>
    </head>
    <body>
        <h1>Обо мне</h1>
        <p>Меня зовут Денис. Я студент GB :).</p>
    </body>
    </html>
    """
    return HttpResponse(html)
