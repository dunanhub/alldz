# my_project/urls.py

from django.contrib import admin
from django.urls import path
from homework import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),  # Страница регистрации
    path('login/', views.login_view, name='login'),  # Страница входа
    path('logout/', views.logout_view, name='logout'),  # Страница выхода
    path('menu/', views.menu, name='menu'),  # Страница выбора специальности и предмета
    path('record_homework/', views.record_homework, name='record_homework'),  # Страница для записи домашки
    path('', views.home, name='home'),  # Главная страница
]
