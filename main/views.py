from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context ={
        'title': 'Blossom - главная'
    }   
    return render(request, 'main/index.html', context)

def about(request):
    context ={
        'title': 'Blossom - О нас',
        
    }   
    
    return render(request, 'main/about.html', context)