# Generated by Django 4.0 on 2022-03-03 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0004_remove_message_is_sent_message_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='is_active',
            field=models.BooleanField(default=True, help_text='укажите, является ли рассылка активной', verbose_name='Активная?'),
        ),
    ]
