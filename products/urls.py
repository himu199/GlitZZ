from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('categories/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('products/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('collections/<slug:collection_slug>/', views.collection_detail, name='collection_detail'),
    path('promotions/<slug:promotion_slug>/', views.promotion_detail, name='promotion_detail'),
    path('shop_now/', views.all_products, name='all_products'),
   path('search/', views.search, name='search'),
]