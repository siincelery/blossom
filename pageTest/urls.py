from django.urls import path
from pageTest import views

app_name = 'personality_test'  # Пространство имен

urlpatterns = [
    path('', views.personality_test, name='pageTest'),  # Главная страница теста
    path('result/', views.result_page_test, name='result'),  # Страница результатов
    path('reset/', views.reset_test, name='reset'),
]