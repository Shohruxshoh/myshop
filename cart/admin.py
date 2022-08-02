from django.contrib import admin
from .models import Cart, CartItems, Product
# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Product)