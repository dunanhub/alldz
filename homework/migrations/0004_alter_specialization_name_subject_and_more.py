# Generated by Django 5.1.3 on 2024-11-28 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialization',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.specialization')),
            ],
        ),
        migrations.AlterField(
            model_name='homework',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.subject'),
        ),
    ]