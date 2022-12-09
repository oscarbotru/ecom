from django.db import models
from django.conf import settings

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    STATUS_NEW = 'new'
    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'

    STATUSES = (
        (STATUS_NEW, 'новая'),
        (STATUS_DRAFT, 'черновик'),
        (STATUS_PUBLISHED, 'опубликовано'),
    )

    title = models.CharField(max_length=150, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое')

    preview = models.ImageField(upload_to='blog', verbose_name='превью', **NULLABLE)

    status = models.CharField(choices=STATUSES, default=STATUS_NEW, max_length=10, verbose_name='статус')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def likes(self):
        return self.like_set.all().count()

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        ordering = ('-created_at',)


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='сатья')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
