
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("The Username must be set")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    json_data = models.JSONField(default=dict)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.username
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization, related_name='subjects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Homework(models.Model):
    task = models.TextField()
    audio_file = models.FileField(upload_to='homework_audio/', null=True, blank=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"Homework for {self.subject.name} in {self.specialization.name}"

class AudioHomework(models.Model):
    file = models.FileField(upload_to='homework_audio/')
    task = models.TextField()  # Дополнительно можно хранить описание задания

    def __str__(self):
        return f"Audio Homework: {self.id}"
