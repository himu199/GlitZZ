from django.contrib import admin
from .models import Category,Product, Collection, Promotion, Review
# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Promotion)
admin.site.register(Review)


