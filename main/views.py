from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Products,Categories
from main.models import Advantage

def index(request):
    
    advantages = Advantage.objects.all()
    # Получаем товары со скидкой
    discounted_products = Products.objects.filter(discount__gt=0)[:3]  # Берем первые 3 товара
    # Создаем контекст с данными
    context = {
        'title': 'Blossom - главная',
        'advantages': advantages,  # Добавляем преимущества в контекст
        'discounted_products': discounted_products,  # Добавляем товары со скидкой в контекст
    }
    
    return render(request, 'main/index.html', context)

def about(request):
    context ={
        'title': 'Blossom - О нас',
        
    }   
    
    return render(request, 'main/about.html', context)