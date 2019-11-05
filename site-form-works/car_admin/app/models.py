from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Машина')
    model = models.CharField(max_length=50, verbose_name='Модель')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')
    title = models.CharField(max_length=100, verbose_name='Модель')
    text = models.TextField(verbose_name='Описание')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'

    def __str__(self):
        return str(self.car) + ' ' + self.title

