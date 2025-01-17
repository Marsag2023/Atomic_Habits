# Atomic_Habits
Реализация бэкенд-часть SPA веб-приложения по книге Джеймса Клира «Атомные привычки»,
которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.
Модели
я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка не должна расходовать на выполнение больше двух минут. Исходя из этого получаем первую модель — «Привычка».

Привычка:
Пользователь — создатель привычки.
Место — место, в котором необходимо выполнять привычку.
Время — время, когда необходимо выполнять привычку.
Действие — действие, которое представляет собой привычка.
Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки

Валидаторы
Исключен одновременный выбор связанной привычки и указания вознаграждения.
В модели нельзя заполнять одновременно и поле вознаграждения, и поле связанной привычки. Можно заполнить только одно из двух полей.
Время выполнения не больше 120 секунд.
В связанные привычки попадают только привычки с признаком приятной привычки.
У приятной привычки нет вознаграждения или связанной привычки.
Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
Нельзя не выполнять привычку более 7 дней. Например, привычка может повторяться раз в неделю, но не раз в 2 недели. За одну неделю необходимо выполнить привычку хотя бы один раз.

Пагинация
Для вывода списка привычек реализована пагинация с выводом по 5 привычек на страницу.

Права доступа
Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

Эндпоинты
Регистрация.
Авторизация.
Список привычек текущего пользователя с пагинацией.
Список публичных привычек.
Создание привычки.
Редактирование привычки.
Удаление привычки.

Интеграция
Для полноценной работы сервиса реализована работа с отложенными задачами для напоминания о том, в какое время какие привычки необходимо выполнять.
Для этого интегрированы сервисы уведомления по электронной почте и в мессенджер Телеграм 

Для запуска проекта необходимо:.

Клонировать репозиторий на компьютер.
Создать базу данных в БД «PostgreSQL».
Создать и заполнить своими данными файл .env. Необходимые для заполнения переменные окружения находятся в файле .env.sample
Установить и подключить виртуальное окружение venv python3 -m venv venv source venv/bin/activate
Суперпользователь создается командой python manage.py csu
Рассылка запускается командами:
redis-server
celery -A config worker —loglevel=info
celery -A config beat —loglevel=info
