import phonenumbers
from phonenumber_field.modelfields import PhoneNumberField

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models


class Mailing(models.Model):
    start_at = models.DateTimeField('Дата и время запуска')
    stop_at = models.DateTimeField('Дата и время окончания')
    text = models.TextField('Текст сообщения')
    mobile_codes = models.CharField(
        'Коды операторов',
        max_length=512,
        blank=True,
        help_text='''укажите коды операторов для рассылки через
        запятую или оставьте поле пустым для рассылки на все номера'''
        )
    tags = models.CharField(
        'Тэги',
        max_length=512,
        blank=True,
        help_text='''укажите тэги клиентов для рассылки через
        запятую или оставьте поле пустым для рассылки всем клиентам'''
        )
    is_active = models.BooleanField(
        'Активная?',
        default=True,
        help_text='укажите, является ли рассылка активной'
        )

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return f'№{self.id} от {self.start_at}'


class Client(models.Model):
    TIME_ZONES = [
        ('UTC+3', 'Europe/Moscow'),
    ]

    phonenumber = PhoneNumberField(
        'Телефон заказчика',
        db_index=True,
        unique=True,
        )

    # данное поле может заполняться автоматически путем парсинга тел. номера
    # FIXME вывод поля оставлен в соответствии с ТЗ, лучше сделать
    # editable=False, нужно решение заказчика.
    mobile_code = models.PositiveSmallIntegerField(
        'Код оператора мобильной связи',
        validators=[MinValueValidator(900), MaxValueValidator(999)],
        blank=True,
        null=True,
        )

    tag = models.CharField(
        'Метка',
        max_length=50,
        blank=True,
        )
    time_zone = models.CharField(
        'Часовой пояс',
        choices=TIME_ZONES,
        max_length=50
        )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.phonenumber}'

    def save(self, *args, **kwargs):
        if not self.mobile_code:
            phone = str(phonenumbers.parse(str(self.phonenumber), None).national_number)
            self.mobile_code = int(phone[:3])
        super().save(*args, **kwargs)


class Message(models.Model):
    sent_at = models.DateTimeField(
        'Дата и время отправки',
        null=True,
        blank=True,
        )
    status = models.PositiveSmallIntegerField(
        'Статус отправки',
        validators=[MinValueValidator(200), MaxValueValidator(599)],
        blank=True,
        null=True,
        )
    mailing = models.ForeignKey(
        Mailing,
        verbose_name='Рассылка',
        on_delete=models.CASCADE,
        related_name='messages',
        )
    client = models.ForeignKey(
        Client,
        verbose_name='Клиент',
        on_delete=models.CASCADE,
        )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.mailing} > {self.client}'
