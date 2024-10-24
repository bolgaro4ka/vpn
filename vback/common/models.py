from django.db import models


# Create your models here.
class Tariff(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    ppm = models.IntegerField(verbose_name='Плата за месяц')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    image = models.ImageField(upload_to='tariffs', blank=True, null=True, verbose_name='Изображение')
    is_published = models.BooleanField(default=False, verbose_name='Опубликован')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'


class Payment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    user = models.ForeignKey('users.PUser', on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return str(self.user.id)
    
    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class Tutorial(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    is_published = models.BooleanField(default=False, verbose_name='Опубликован')
    image = models.ImageField(upload_to='tutorials', blank=True, null=True, verbose_name='Изображение')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    url = models.CharField(max_length=255, verbose_name='Ссылка', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Туториал'
        verbose_name_plural = 'Туториалы'