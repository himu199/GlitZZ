from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug =  AutoSlugField(populate_from='name', unique=True, blank=True)
    image= models.ImageField(upload_to='static/images/',null=True,blank=True)
    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200,unique=True, default='')
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    
    def __str__(self):
        return self.name



class Collection(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True, blank=True)
    description = models.TextField()
    year= models.DateTimeField()
    
   
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    promotion = models.ForeignKey(Promotion, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.OneToOneField(Category, on_delete=models.PROTECT)
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    
    def __str__(self):
        return self.name



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    image = models.ImageField(upload_to='images/review/', null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.rating} Star Review for {self.product.name}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="product_images")
    image =  models.ImageField(upload_to="static/images/")


# Create your models here.
