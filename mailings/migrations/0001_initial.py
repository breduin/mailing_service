# Generated by Django 4.0 on 2022-03-01 18:48

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region=None, verbose_name='Телефон заказчика')),
                ('tag', models.CharField(blank=True, max_length=50, verbose_name='Метка')),
                ('time_zone', models.CharField(choices=[('UTC+3', 'Europe/Moscow')], max_length=50, verbose_name='Часовой пояс')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateTimeField(verbose_name='Дата и время запуска')),
                ('stop_at', models.DateTimeField(verbose_name='Дата и время окончания')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время отправки')),
                ('is_sent', models.BooleanField(default=False, verbose_name='Отправлено?')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.client', verbose_name='Клиент')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
