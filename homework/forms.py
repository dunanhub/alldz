from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django import forms
from .models import Homework, Specialization, Subject

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

# Вход

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', 'home')  # Перенаправление на 'home', если next не указан
            return HttpResponseRedirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'homework/login.html', {'form': form})

# Выход
def logout_view(request):
    logout(request)  # Выход из системы
    return redirect('home')  # Перенаправляем на главную страницу
# homework/forms.py
class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['specialization', 'subject', 'task']

    # Делаем выбор специализации и предмета динамическим
    specialization = forms.ModelChoiceField(queryset=Specialization.objects.all(), label="Specialization")
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), label="Subject")

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['specialization', 'subject', 'task', 'audio_file']

    #
