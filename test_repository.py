from session_factory import SessionFactory
from repositories import BookRepository
from models import Book

# Создаём сессию
session = SessionFactory()

# Создаём репозиторий
book_repo = BookRepository(session)

# Тест 1: Добавление книги
new_book = Book(title="Test Book", author_id=1)
book_repo.add_book(new_book)

# Тест 2: Получение книг автора
author_books = book_repo.get_books_by_author(1)
print("Книги автора с ID 1:")
for book in author_books:
    print(f" - {book.title}")

# Тест 3: Удаление книги
if author_books:
    book_id_to_delete = author_books[0].id
    book_repo.delete_book(book_id_to_delete)