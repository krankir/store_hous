from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная!',
        'content': 'тут будет контент когда то, думаю завтра!',
        'categories': categories
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'Ajax (от англ. Asynchronous Javascript and XML — «асинхронный JavaScript и XML») — подход к построению интерактивных пользовательских интерфейсов веб-приложений,'
    }
    return render(request, 'main/about.html', context=context)
