from django.contrib import admin
from .models import ProductCarousel, CollectionCarousel, PromotionCarousel

# Register your models here.
admin.site.register(ProductCarousel)
admin.site.register(CollectionCarousel)
admin.site.register(PromotionCarousel)
