# urls.py
from django.urls import path
from homework import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),  # Страница регистрации
    path('login/', views.login_view, name='login'),  # Страница входа
    path('logout/', views.logout_view, name='logout'),  # Страница выхода
    path('menu/', views.menu, name='menu'),  # Страница выбора специальности и предмета
    path('record_homework/', views.record_homework, name='record_homework'),  # Страница записи домашки
    path('', views.home, name='home'),  # Главная страница, которая всегда показывается при переходе на '/'
    path('homework_for_subject/<int:subject_id>/', views.homework_for_subject, name='homework_for_subject'),    path('delete_homework/<int:homework_id>/', views.delete_homework, name='delete_homework'),
]
