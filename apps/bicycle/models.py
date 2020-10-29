from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Bicycle(models.Model):
    name = models.CharField('Название модели', max_length=30)

    pic = models.ImageField('Фотография модели', upload_to='static/bicycles/images/')

    made_in = models.CharField('Производство', max_length=20)
    speeds_number = models.IntegerField('Количество скоростей')

    frame_type = models.CharField('Тип рамы', max_length=20)
    frame_size = models.IntegerField('Размер рамы', validators=[
        MaxValueValidator(40)
    ])

    wheel_type = models.CharField('Тип рамы', max_length=20)
    wheel_size = models.IntegerField('Размер колес', validators=[
        MaxValueValidator(40)
    ])

    available = models.BooleanField('Наличие', default=True)

    description = models.CharField('Описание модели', max_length=100)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.name
