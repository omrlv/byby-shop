# Generated by Django 3.0.8 on 2020-08-09 06:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bicycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название модели')),
                ('pic', models.ImageField(upload_to='static/bicycles/images/', verbose_name='Фотография модели')),
                ('made_in', models.CharField(max_length=20, verbose_name='Производство')),
                ('speeds_number', models.IntegerField(verbose_name='Количество скоростей')),
                ('frame_type', models.CharField(max_length=20, verbose_name='Тип рамы')),
                ('frame_size', models.IntegerField(validators=[django.core.validators.MaxValueValidator(40)], verbose_name='Размер рамы')),
                ('wheel_type', models.CharField(max_length=20, verbose_name='Тип рамы')),
                ('wheel_size', models.IntegerField(validators=[django.core.validators.MaxValueValidator(40)], verbose_name='Размер колес')),
                ('available', models.BooleanField(default=True, verbose_name='Наличие')),
                ('description', models.CharField(max_length=100, verbose_name='Описание модели')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
        ),
    ]