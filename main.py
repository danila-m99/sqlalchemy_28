from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from models import Base, Author, Book, User
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

# Получаем строку подключения из переменной среды
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("Строка подключения к базе данных не найдена в .env файле")

# Создаём движок и сессию
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Логирование запросов (для сравнения SQL-запросов)
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# 1. Добавление данных в базу
def add_sample_data():
    author1 = Author(name="J.K. Rowling")
    author2 = Author(name="George R.R. Martin")
    session.add_all([
        author1,
        author2
    ])
    session.flush()  # Чтобы получить id авторов для книг

    book1 = Book(title="Harry Potter and the Philosopher's Stone", author_id=author1.id)
    book2 = Book(title="Harry Potter and the Chamber of Secrets", author_id=author1.id)
    book3 = Book(title="A Game of Thrones", author_id=author2.id)
    book4 = Book(title="A Clash of Kings", author_id=author2.id)
    session.add_all([book1, book2, book3, book4])
    session.commit()

# 2. Ленивая загрузка (Lazy loading)
def lazy_loading_example():
    authors = session.query(Author).all()
    for author in authors:
        print(f"Author: {author.name}")
        print("Books:")
        for book in author.books:  # Это вызовет отдельный запрос для каждой книги
            print(f" - {book.title}")

# 3. Жадная загрузка (Eager loading)
def eager_loading_example():
    authors = session.query(Author).options(joinedload(Author.books)).all()
    for author in authors:
        print(f"Author: {author.name}")
        print("Books:")
        for book in author.books:  # Данные книг уже загружены
            print(f" - {book.title}")

# Выполнение
if __name__ == "__main__":
    print("Добавление данных...")
    add_sample_data()
    print("\nЛенивая загрузка:")
    lazy_loading_example()
    print("\nЖадная загрузка:")
    eager_loading_example()