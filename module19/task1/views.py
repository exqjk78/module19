from django.shortcuts import render
from .forms import UserRegister
from .models import *
# Create your views here.
def sign_up_by_django(req):
    users = Buyer.objects.all()
    names = []
    for user in users:
        names.append(user.name)
    info = {}
    if req.method == "POST":
        form = UserRegister(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in names:
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username,balance=0,age=age)
                info['message'] = f'Приветствуем, {username}!'
        else:
            info['form'] = form
    else:
        form = UserRegister()
    info['form'] = form
    return render(req, 'registration_page.html', info)

def platform(req):
    title = 'Главная'
    main_page = 'Главная страница'
    context = {'title': title,
               'main_page': main_page
    }
    return render(req, 'platform.html', context)

def shop_page(req):
    title = 'Магазин'
    shop_title = 'Игры'
    buy = 'Купить.'
    games = Game.objects.all()
    context = {'shop_title': shop_title,
               'games': games,
               'buy': buy,
               'title': title
    }
    return render(req, 'shop.html', context)

def cart_page(req):
    message = 'Ваша корзина пуста, а то что вы не можете в неё ничего положить уже не наши проблемы :3'
    title = 'Корзина'
    context = {'message': message,
               'title': title
    }
    return render(req, 'cart.html', context)

