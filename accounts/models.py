from django.contrib.auth.models import User,AbstractUser,Group,Permission, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
from django.conf import settings




class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='addresses')
    street_address = models.CharField(_('street address'), max_length=100)
    city = models.CharField(_('city'), max_length=100)
    state = models.CharField(_('state'), max_length=100)
    country = models.CharField(_('country'), max_length=100)

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}, {self.country}"


#order models
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField('products.Product', through='OrderItem')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.CharField(max_length=200)
    billing_address = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=(
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered')
    ))

class OrderItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

#cart models
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in cart {self.cart.cart_id}"

    @property
    def price(self):
        return self.product.price

    @property
    def total_price(self):
        return self.price * Decimal(self.quantity)


#wishlist
class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('products.Product', blank=True, related_name='wishlists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
#search-history
class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anonymous_user_id = models.CharField(max_length=255, null=True, blank=True)
    query = models.CharField(max_length=100)
    search_date = models.DateTimeField(auto_now_add=True)




