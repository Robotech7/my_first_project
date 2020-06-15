from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор', default=get_user_model())
    title = models.CharField(max_length=200, verbose_name='Заголовок', unique=True)
    text = RichTextUploadingField(verbose_name='Текст')
    date = models.DateField(auto_now=True, verbose_name='Дата')
    slug = models.SlugField(max_length=35, unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='post/', blank=True, null=True,
                              verbose_name='Заставка')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:news_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время')

    def __str__(self):
        return f'{self.author}: {self.post}'
