from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Client
from .models import Product
from .models import Order

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Client)
