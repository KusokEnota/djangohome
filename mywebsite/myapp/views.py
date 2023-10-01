from django.http import HttpResponse
from django.shortcuts import render
from .models import Client
from .models import Order

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
