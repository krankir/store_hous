from django.shortcuts import render

from goods.models import Products


def catalog(request):
    goods = Products.objects.all()
    context = {
        'title': 'Home - каталог',
        'goods': goods

    }
    return render(request, 'goods/catalog.html', context=context)


def product(request, product_slug):
    product_ = Products.objects.get(slug=product_slug)

    context = {
        'product': product_
    }

    return render(request, 'goods/product.html', context=context)
