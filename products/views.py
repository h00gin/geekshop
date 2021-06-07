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


def products(request):
    title = 'GeekShop - Каталог'
    header = 'GeekShop'
    list_link = ProductCategory.objects.all()
    goods = Product.objects.all()
    content = {'title': title, 'header': header, 'list_link': list_link, 'goods': goods}
    return render(request, 'products/products.html', content)
