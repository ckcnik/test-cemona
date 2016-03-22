# Проект Cemona

Это подробная документация по проекту. Если какая-то информация устарела или не написана - просьба сообщить об этом, а еще лучше - исправить самому.

## Используемый стек технологий

* Фрэймворк [Django1.8.9](https://www.djangoproject.com/).
* СУБД [PostgreSQL9.4](http://www.postgresql.org/).
* [Python3.4](https://www.python.org/) - язык общего назначения.
* [Nginx](http://nginx.org/ru/) - сервер для отдачи статики.
* [WSGI HTTP Server](http://gunicorn.org/) - для проекта на релизе.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
