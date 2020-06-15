from django.contrib.auth import get_user_model
from django.db import models


class Message(models.Model):
    STATUS = ((1, 'OK'),
              (2, 'Error'),
              (3, 'Pending'))

    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, verbose_name='Автор', null=True)
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст сообщения')
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=3, verbose_name='Статус отправки')
    error = models.TextField(null=True, default=None, verbose_name='Ошибка')

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'

    def __str__(self):
        return f'{self.author}: {self.title}'
