from django.shortcuts import render
from .models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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


def products(request, category_id=None, page=1):
    context = {'header': 'GeekShop', 'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)
