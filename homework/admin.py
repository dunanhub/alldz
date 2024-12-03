
# homework/admin.py
from django.contrib import admin
from .models import Specialization, Subject

# Регистрация моделей в админке
admin.site.register(Specialization)
admin.site.register(Subject)
