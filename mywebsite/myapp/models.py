from django.db import models
from django.utils import timezone

class MyModel(models.Model):
    field1 = models.CharField(max_length=255)
    field2 = models.IntegerField()
    field3 = models.DateField()

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='product_photos/')

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)
    id = models.AutoField(primary_key=True)

    def order_detail(request, order_id):
        order = Order.objects.get(pk=order_id)

        if order.products.exists():
            product = order.products.first()
        else:
            product = None

        return render(request, 'client_orders_list.html', {'order': order, 'product': product})
