from django.db import models


class ChooseMostSold(models.Model):
    first_bike_id = models.IntegerField('id велосипеда №1')
    second_bike_id = models.IntegerField('id велосипеда №2')

    def __str__(self):
        return f'Два самых продаваемых велосипеда'


class Contact(models.Model):
    name = models.CharField('Ваше имя', max_length=50)
    email = models.EmailField('Ваша почта')
    phone = models.CharField('Ваш телефон', max_length=15)

    def __str__(self):
        return f"Данные от {self.name}"
