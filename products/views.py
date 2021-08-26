from django.shortcuts import render

from .models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.cache import cache


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_products():
    if settings.LOW_CACHE:
        key = 'products_list'
        products_list = cache.get(key)
        if products_list is None:
            products_list = Product.objects.all()
            cache.set(key, products_list)
        return products_list
    else:
        return Product.objects.all()


def get_products_by_category(pk):
    if settings.LOW_CACHE:
        key = f'products_by_category_pk_{pk}'
        products_list = cache.get(key)
        if products_list is None:
            products_list = Product.objects.filter(category__pk=pk)
            cache.set(key, products_list)
        return products_list
    else:
        return Product.objects.filter(category__pk=pk)


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
    links_menu = get_links_menu()
    context = {'header': 'GeekShop', 'title': 'GeekShop - Каталог', 'links_menu': links_menu, 'categories': ProductCategory.objects.all()}
    # products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    products = get_products_by_category(category_id) if category_id else get_products()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)
