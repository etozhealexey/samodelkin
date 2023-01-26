from django.db import models


# Create your models here.

class Clients(models.Model):
    auto = models.CharField('Автомобиль', max_length=20)
    telephone = models.CharField('Номер телефона', max_length=20, primary_key=True)
    name = models.CharField('Имя', max_length=100)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural =  'Клиенты'

        def __str__(self):
            return self.title


class Visits(models.Model):
    auto = models.CharField('Автомобиль', max_length=20)
    telephone = models.CharField('Номер телефона', max_length=20, primary_key=True)
    name = models.CharField('Имя', max_length=100)
    time_start = models.DateTimeField('Дата начала работы', auto_now=True)
    time_end = models.DateTimeField('Дата окончания работы', auto_now=True)

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'

        def __str__(self):
            return self.title





