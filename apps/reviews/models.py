from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Review(models.Model):
    name = models.CharField('Ваше имя', max_length=50)

    text = models.CharField('Текст вашего отзыва', max_length=200)

    class Meta:
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text[:10]
