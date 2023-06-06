from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Collection, Promotion, Review


# Create your views here.
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        'name': category.name,
        'category': category,
        'products': products
    }
    return render(request, 'templates/category_detail.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    reviews = product.reviews.all()
    context = {'product': product, 'reviews': reviews}
    return render(request, 'templates/product_detail.html', context)


def collection_detail(request, slug):
    collection = get_object_or_404(Collection, slug=slug)
    products = collection.product_set.all()
    context = {'name': collection.name,'collection': collection, 'products': products}
    return render(request, 'templates/collection_detail.html', context)

def promotion_detail(request, slug):
    promotion = get_object_or_404(Promotion, slug=slug)
    products = promotion.product_set.all()
    context = {'name': promotion.title,'promotion': promotion, 'products': products}
    return render(request, 'templates/promotion_detail.html', context)


def all_products(request):
    products = Product.objects.all()
    context = {'name': 'All Products','products': products}
    return render(request, 'templates/all_products.html', context)


def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'templates/search_results.html', context)
