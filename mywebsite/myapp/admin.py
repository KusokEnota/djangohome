# admin.py
from django.contrib import admin
from .models import Client, Product, Order, MyModel
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'photo']

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')
    list_filter = ('field1', 'field2')
    search_fields = ('field1', 'field2')


admin.site.index_template = 'admin/custom_admin.html'
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Client)
