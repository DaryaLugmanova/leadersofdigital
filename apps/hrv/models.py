from django.db import models


class HRV(models.Model):
    MALE = 'Мужской'
    FEMALE = 'Женский'

    SEX_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]
    age = models.PositiveIntegerField(verbose_name='Возраст')
    sex = models.CharField(verbose_name='Пол', max_length=15, choices=SEX_CHOICES)
    hrv_with_rules = models.BooleanField(verbose_name='Ритмограмма выполнена по правилам', default=False)
    hrv_file = models.FileField(verbose_name='Файл с ритмограммой', upload_to='hrv/%Y/%m/%d/', default=None)

    class Meta:
        verbose_name = 'Данные ритмограммы'
        verbose_name_plural = 'Ритмограммы'
