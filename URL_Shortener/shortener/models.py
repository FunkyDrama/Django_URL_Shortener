from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User



class Person(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=CASCADE, verbose_name='Пользователь')
    profile_pic = models.ImageField(null=True, blank=True, default='default.png', upload_to='user_images', verbose_name='Изображение профиля')
    name = models.CharField(max_length=200, null=True, verbose_name='Имя')
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name='E-mail пользователя')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Профиль пользователя {self.name}'
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class URLS(models.Model):
    long_url = models.URLField(max_length=200, null=True, blank=True, verbose_name='Длинная ссылка')
    short_url = models.URLField(max_length=200, null=True, blank=True, verbose_name='Короткая ссылка')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True, verbose_name='Создатель')
    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')

    def __str__(self):
        return self.short_url
    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'