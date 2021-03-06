# Сервис рассылки сообщений

*API, интеграция с внешним сервисом*


## Инструменты

Python, Django, Redis


## Краткое описание

Основые сущности сервиса: Mailing, Client и Message. Рассылка осуществляется на телефонные номера
клиентов в соответствии с заданными фильтрами. Для Mailing и Client сервис предоставляет набор CRUD-операций
с помощью API либо через веб-интерфейс. Экземпляры Message создаются автоматически при осуществлении
рассылки и содержат информацию, необходимую для создания отчётов по рассылкам.

## Логика работы сервиса

После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания -  из справочника выбираются все клиенты, которые подходят под значения фильтра, указанного в этой рассылке и запускается отправка для всех этих клиентов.

Рассылка может быть запущена также через API направлением соответствующего запроса.

API также предоставляет возможность получения сводных данных по рассылкам: количество активных рассылок, количество отправленных сообщений и т.п.

## Как установить

Код является свободным, ты можешь установить его и пользоваться. Для этого тебе понадобится:

1. Установить Python 3.10+. [см. как установить (англ.)](https://realpython.com/installing-python/), а [здесь для Debian-based (рус.)](http://userone.ru/?q=node/41).

2. Установить и запустить [Redis](https://redis.io/topics/quickstart).


Далее, скачай репозиторий к себе, установи и активируй виртуальное окружение:
```
    python3 -m venv env
    source env/bin/activate
```
перейди в папку проекта, установи необходимые библиотеки, указанные в файле requirements.txt:
```
    pip install -r requirements.txt
```
создай папку logs, в ней будут располагаться лог-файлы сервиса:
```
    mkdir logs
```
запусти миграции:
```
    ./manage.py migrate
```
создай суперпользователя сервиса:
```
    ./manage.py createsuperuser
```
Запусти проект:

```
    ./manage.py runserver
```

## Описание API

Открой браузер и укажи в адресной строке:
```
http://127.0.0.1:8000/docs/
```
Откроется страница с описанием API сервиса. С этой страницы можно отправить запрос и посмотреть ответ
сервиса.
для доступа к административной части сайта укажи в адресной строке браузера
```
http://127.0.0.1:8000/admin/
```
далее, укажи данные суперпользователя, созданного несколькими шагами ранее.


Для интеграции с разрабатываемым проектом  существует внешний сервис, который может принимать запросы на отправку сообщений в сторону клиентов.

[Внешний API сервис](https://probe.fbrq.cloud/docs)
