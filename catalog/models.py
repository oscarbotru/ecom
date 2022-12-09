from django.db import models

from catalog.service import notification_to_user


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    count = models.PositiveSmallIntegerField(default=0, verbose_name='остаток на складе')
    is_deleted = models.BooleanField(default=False, verbose_name='удален')

    views = models.PositiveIntegerField(default=0, verbose_name='просмотры')
    # TODO: количество просмотров

    def save(self, *args, **kwargs):
        print(self.__dict__)
        if self.pk is not None:
            old_state = self.__class__.objects.get(pk=self.pk)
            if old_state.count == 0 and self.count > 0:
                notification_to_user(self.pk)
                self.is_deleted = False
            else:
                if self.count == 0:
                    self.is_deleted = True

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.title}'

    # def delete(self, *args, **kwargs):
    #     self.is_deleted = True
    #     self.save()
