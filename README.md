# API Yatube: Социальная сеть для публикации дневников

API Yatube предоставляет полный функционал работы с приложением:

- Просмотр, создание / редактирование / удаление постов;
- Комментирование постов;
- Просмотр списка существующих сообществ и информации о них;
- Подписываться и следить за активностью других авторов.

Просмотр постов, сообществ и комментариев доступен, в том числе, для
неавторизованных пользователей.

## Технологии

- **Python 3.9**
- **Django 3.2**
- **Django REST framework 3.12**
- **SQLite3**
- **JWT**


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/your-repo/diaries_api.git
```
```bash
cd diaries_api
```

Создать и активировать виртуальное окружение:
```bash
python -m venv env
```
```bash
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
python3 manage.py migrate
```

Запустить проект:
```bash
python3 manage.py runserver
```


## Эндпоинты API

- `api/v1/jwt/create/` \
Если вы уже зарегистрированы на платформе, то можете получить jwt-токен \
Пример ответа:
  ```json
  {
    "refresh": "string",
    "access": "string"
  }
  ```

- `api/v1/posts/` \
  Получаем список всех постов или создаём новый пост (GET, POST) \
  Пример ответа на POST запрос:
  ```json
  {
    "id": "integer",
    "author": "string",
    "text": "string",
    "pub_date": "string (date-time)",
    "image": "string (binary, nullable)",
    "group": "integer (nullable)"
  }
  ```

- `api/v1/posts/{post_id}/` \
  Получаем, редактируем или удаляем пост по id (GET, PUT, PATCH, DELETE)


- `api/v1/groups/` \
  Получаем список всех групп (GET)


- `api/v1/groups/{group_id}/` \
  Получаем информацию о группе по id (GET) \
  Пример ответа:
  ```json
  {
    "id": "integer",
    "title": "string",
    "slug": "string",
    "description": "string"
  }
  ```

- `api/v1/posts/{post_id}/comments/` \
  Получаем список всех комментариев поста с id=post_id или создаём новый, 
указав id поста, который хотим прокомментировать (GET, POST)


- `api/v1/posts/{post_id}/comments/{comment_id}/` \
  Получаем, редактируем или удаляем комментарий по id у поста с id=post_id 
(GET, PUT, PATCH, DELETE) \
  Пример ответа на GET, PUT, PATCH запросы:
  ```json
  {
    "id": "integer",
    "author": "string",
    "text": "string",
    "created": "string (date-time)",
    "post": "integer"
  }
  ```

- `api/v1/follow/` \
  Получаем список ваших подписок, а также создаем новую (GET, POST)\
  Пример ответа на GET запрос:
  ```json
  {
    "user": "string",
    "following": "string"
  }
  ```

- `redoc/` \
  **Более подробная информация о запросах, требованиях к ним и примеров доступна
по адресу**

---
## Автор проекта
[skhfh](https://github.com/skhfh)