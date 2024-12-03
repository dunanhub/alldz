from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import HomeworkForm
from .models import Specialization, Subject, Homework, AudioHomework
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
def home(request):
    if request.user.is_authenticated:
        return redirect('record_homework')  # Если пользователь авторизован, перенаправляем на страницу записи домашки
    return render(request, 'homework/home.html')  # Если не авторизован, показываем формы для входа/регистрации

# Регистрация
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  # Авторизация после регистрации
            return redirect('menu')  # Перенаправляем на страницу записи домашки
    else:
        form = UserRegistrationForm()
    return render(request, 'homework/register.html', {'form': form})

# Вход
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Логиним пользователя
            return redirect('menu')  # Перенаправляем на страницу записи домашки
    else:
        form = AuthenticationForm()
    return render(request, 'homework/login.html', {'form': form})

# Выход
def logout_view(request):
    logout(request)  # Выход из системы
    return redirect('home')  # Перенаправляем на главную страницу после выхода
def menu(request):
    specializations = Specialization.objects.all()
    return render(request, 'homework/menu.html', {'specializations': specializations})

def homework_for_subject(request, subject_id):
    # Получаем домашки для выбранного предмета
    homeworks = Homework.objects.filter(subject_id=subject_id)
    homework_data = []
    
    for homework in homeworks:
        homework_data.append({
            'subject_name': homework.subject.name,
            'task': homework.task,
            'audio': homework.audio.url if homework.audio else None,
        })
    
    return JsonResponse({'homeworks': homework_data})
def record_homework(request):
    if request.method == 'POST':
        # Обрабатываем аудио
        if 'audio' in request.FILES:
            audio_file = request.FILES['audio']
            task_description = request.POST.get('task', '')
            specialization_id = request.POST.get('specialization')
            subject_id = request.POST.get('subject')

            specialization = Specialization.objects.get(id=specialization_id)
            subject = Subject.objects.get(id=subject_id)

            # Сохраняем аудио файл и домашку
            homework = Homework.objects.create(
                specialization=specialization,
                subject=subject,
                task=task_description,
                audio_file=audio_file
            )

            return JsonResponse({'message': 'Audio uploaded successfully!'})

    # В случае GET запроса возвращаем форму для записи домашки
    specializations = Specialization.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'homework/record_homework.html', {
        'specializations': specializations,
        'subjects': subjects
    })


def home(request):
    if request.user.is_authenticated:
        return redirect('menu')  # Если пользователь уже вошел, редиректим на страницу меню
    return render(request, 'homework/home.html')  # 
def get_homework_for_subject(request, subject_id):
    homeworks = Homework.objects.filter(subject_id=subject_id)
    homework_data = []
    for homework in homeworks:
        homework_data.append({
            'id': homework.id,
            'task': homework.task,
            'subject_name': homework.subject.name,
            'audio': homework.audio.url if homework.audio else None,
        })
    return JsonResponse({'homeworks': homework_data})

# Удаление домашнего задания
def delete_homework(request, homework_id):
    try:
        homework = Homework.objects.get(id=homework_id)
        subject_id = homework.subject.id
        homework.delete()
        return JsonResponse({'message': 'Homework deleted successfully!', 'subject_id': subject_id})
    except Homework.DoesNotExist:
        return JsonResponse({'message': 'Homework not found'}, status=404)