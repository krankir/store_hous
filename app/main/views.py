from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Главная!',
        'content': 'тут будет контент когда то, думаю завтра!',
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'Ajax (от англ. Asynchronous Javascript and XML — «асинхронный JavaScript и XML») — подход к построению интерактивных пользовательских интерфейсов веб-приложений,'
    }
    return render(request, 'main/about.html', context=context)
