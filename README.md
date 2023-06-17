# Kollok2


# Установка и запуск
1) Установите Python на свой компьютер
2) `pip install django`
3) Из корневой папки проекта: `cd games`
4) `python manage.py runserver`
5) после этого к адресу добавляете games/ или players/ (пример http://127.0.0.1:8000/games/) и оно выдает что просите

# Взаимодействие с сервером
Было принято решение использовать встроенный инструмент `curl`

## Использование (примеры командны из терминала)
* `curl -X POST localhost:8000/players/`
* `curl -X GET localhost:8000/games/2/`
* `curl -X PUT --data "state=walk&player_id=2&score=13" localhost:8000/games/3/`

