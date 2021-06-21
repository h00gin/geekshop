from django.shortcuts import render
from .models import ProductCategory, Product


# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'GeekShop Store',
        'paragraph': 'Новые образы и лучшие бренды на GeekShop Store. '
                     'Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд.'
                     ' -20% новым покупателям.',
        'purchases': 'Начать покупки',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {'header': 'GeekShop', 'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    context.update({
        'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    })
    return render(request, 'products/products.html', context)
