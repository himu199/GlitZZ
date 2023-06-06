from django.contrib import admin
from .models import Address, Order,  OrderItem, Payment, Cart, CartItem, Wishlist, Search

# Register your models here.
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(Search)



