1. Задача 1

Анализ результатов
1. Ленивая загрузка (Lazy loading)
SQL-запросы:
Один запрос для загрузки авторов.
Для каждой книги автора выполняется отдельный запрос.
Преимущества:
Экономия ресурсов при загрузке данных, если связанные записи (например, книги) не используются.
Недостатки:
Может привести к множеству SQL-запросов при доступе ко всем связанным данным (так называемая проблема N+1 запросов).
2. Жадная загрузка (Eager loading)
SQL-запросы:
Один запрос для загрузки авторов и их книг с использованием JOIN.
Преимущества:
Уменьшение количества запросов к базе данных.
Удобно для случаев, когда связанные данные (например, книги) точно будут использоваться.
Недостатки:
Загрузка лишних данных, если связанные записи не используются.

SQL-запросы в логах
1. Логи для ленивой загрузки (Lazy Loading)
SQL-запросы:

Первый запрос:

SELECT authors.id AS authors_id, authors.name AS authors_name
FROM authors;
Загружает всех авторов из таблицы authors.
Этот запрос выполняется один раз.

Последующие запросы:

SELECT books.id AS books_id, books.title AS books_title, books.author_id AS books_author_id
FROM books
WHERE %(param_1)s = books.author_id;
Выполняется для каждой записи из таблицы authors для получения книг конкретного автора (WHERE books.author_id = ...).
Например:
Для J.K. Rowling: один запрос, чтобы получить её книги.
Для George R.R. Martin: другой запрос.
Общее количество запросов:

1 запрос для загрузки авторов.
1 запрос для каждой группы книг (зависит от количества авторов).

2. Задача 2

Ошибка при добавлении пользователей:

Из-за повторяющегося значения email транзакция была откатана.
SQLAlchemy вызвал ROLLBACK, отменив все изменения.
Таблица users осталась пустой:

Это подтверждается запросом, который не возвращает записей в таблице.

Ограничение UNIQUE для столбца email успешно настроено.
Механизм транзакций работает корректно: при ошибке данные не добавляются.

Транзакция с пользователями:
INFO:sqlalchemy.engine.Engine:select pg_catalog.version()
INFO:sqlalchemy.engine.Engine:[raw sql] {}
INFO:sqlalchemy.engine.Engine:select current_schema()
INFO:sqlalchemy.engine.Engine:[raw sql] {}
INFO:sqlalchemy.engine.Engine:show standard_conforming_strings
INFO:sqlalchemy.engine.Engine:[raw sql] {}
INFO:sqlalchemy.engine.Engine:BEGIN (implicit)
INFO:sqlalchemy.engine.Engine:INSERT INTO users (username, email) SELECT p0::VARCHAR, p1::VARCHAR FROM (VALUES (%(username__0)s, %(email__0)s, 0), (%(username__1)s, %(email__1)s, 1), (%(username__2)s, %(email__2)s, 2)) AS imp_sen(p0, p1, sen_counter) ORDER BY sen_counter RETURNING users.id, users.id AS id__1
INFO:sqlalchemy.engine.Engine:[generated in 0.00007s (insertmanyvalues) 1/1 (ordered)] {'email__0': 'user1@example.com', 'username__0': 'user1', 'email__1': 'user2@example.com', 'username__1': 'user2', 'email__2': 'user1@example.com', 'username__2': 'user3'}
INFO:sqlalchemy.engine.Engine:ROLLBACK
Ошибка при добавлении пользователей. Все изменения откатились.
INFO:sqlalchemy.engine.Engine:BEGIN (implicit)
INFO:sqlalchemy.engine.Engine:SELECT users.id AS users_id, users.username AS users_username, users.email AS users_email
FROM users
INFO:sqlalchemy.engine.Engine:[generated in 0.00044s] {}

3. Задача 3

Краткое описание шагов и выводы
1. Инициализация Alembic
Шаг: Настроен Alembic с указанием Base.metadata для автоматической генерации миграций.
Вывод: Alembic корректно интегрирован в проект.
2. Создание таблицы orders
Шаг: Добавлена модель Order в models.py и создана миграция для её добавления.
Вывод: Таблица успешно создана в базе данных с полями id, product_name, quantity, и created_at.
3. Модификация таблицы orders
Шаг: Добавлено поле price, удалено поле created_at через новую миграцию.
Вывод: Изменения применены к структуре таблицы.
4. Откат изменений
Шаг: Выполнен откат миграции, чтобы проверить возврат к предыдущему состоянию.
Вывод: Структура таблицы успешно восстановлена (удалено поле price, возвращено created_at).
5. Проверка работы Alembic
Шаг: На каждом этапе проверялась структура таблицы через DBeaver и SQL-запросы.
Вывод: Alembic корректно фиксирует изменения и управляет структурой таблиц.
Общий вывод
Вы освоили базовые принципы работы с Alembic: создание таблиц, модификация структуры и откат изменений.
Таблица orders была успешно создана, изменена и возвращена к исходному состоянию.
Этот процесс демонстрирует важность миграций для управления структурой базы данных в командной разработке.

4. Задача 4

Краткое описание шагов и выводы
1. Создание фабрики сессий
Шаг: Настроена фабрика сессий SessionFactory в session_factory.py для подключения к базе данных через SQLAlchemy.
Вывод: Подключение к базе данных через переменные окружения .env работает корректно.
2. Реализация репозитория
Шаг: Создан класс BookRepository в repositories.py с методами:
add_book: добавление новой книги.
get_books_by_author: получение всех книг автора по ID.
delete_book: удаление книги по ID.
Вывод: Логика работы с таблицей books изолирована в репозитории.
3. Тестирование репозитория
Шаг: Написаны и выполнены тестовые сценарии в test_repository.py:
Добавление книги Test Book.
Получение книг автора с ID 1.
Удаление книги с ID 1.
Вывод: Все операции выполнены успешно, база данных обновляется корректно.
4. Отладка путей и модулей
Шаг: Проверены пути импорта и добавлена отладочная информация.
Вывод: Все модули корректно подключены, ошибок импорта больше нет.
Общий вывод
Репозиторий успешно реализован, методы работают корректно.
Тесты подтвердили правильность работы сессий и базы данных.
Работа с базой данных через переменные окружения безопасна и удобна.