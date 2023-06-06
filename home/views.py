from django.shortcuts import render

from .models import ProductCarousel, CollectionCarousel, PromotionCarousel
def homepage(request):
    # Fetch featured collections
    product_carousels = ProductCarousel.objects.all()
    collection_carousels = CollectionCarousel.objects.all()
    promotion_carousels = PromotionCarousel.objects.all()

    context = {
        'product_carousels': product_carousels,
        'collection_carousels': collection_carousels,
        'promotion_carousels': promotion_carousels
    }

    return render(request, 'templates/index.html', context)


# Create your views here.
