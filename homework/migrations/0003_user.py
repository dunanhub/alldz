# Generated by Django 5.1.3 on 2024-11-28 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_specialization_homework'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
