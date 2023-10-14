from django.http import HttpResponse
from .models import Client
from django.shortcuts import render, redirect
from .models import Order, Product
from django.utils.timezone import now, timedelta
from .forms import ProductForm


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

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

def client_orders_list(request, order_id=None):
    current_date = now()
    last_week_start = current_date - timedelta(days=7)
    last_month_start = current_date - timedelta(days=30)
    last_year_start = current_date - timedelta(days=365)

    last_week_products = Product.objects.filter(order__order_date__gte=last_week_start)
    last_month_products = Product.objects.filter(order__order_date__gte=last_month_start)
    last_year_products = Product.objects.filter(order__order_date__gte=last_year_start)

    if order_id is not None:
        order = Order.objects.get(pk=order_id)
        product = Product.objects.get(pk=product_id)  # Здесь нужно получить product_id из запроса или иного источника
    else:
        order = None
        product = None

    return render(request, 'client_orders_list.html', {
        'last_week_products': last_week_products,
        'last_month_products': last_month_products,
        'last_year_products': last_year_products,
        'order': order,
        'product': product,
    })



def home(request):
    return render(request, 'home/home.html')

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
