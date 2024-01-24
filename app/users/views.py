from django.shortcuts import render


def login(request):
    context = {
        'title': 'Авторизация'
    }
    return render(request, 'users/login.html', context=context)


def registration(request):
    context = {
        'title': 'registration'
    }
    return render(request, 'users/registration.html', context=context)


def profile(request):
    context = {
        'profile': 'profile'
    }
    return render(request, 'users/profile.html', context=context)


def logout(request):
    context = {
        'logout': 'logout'
    }
    return render(request, '', context=context)
