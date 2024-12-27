from sqlalchemy.orm import Session
from models import Book

class BookRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_book(self, book: Book):
        """Добавление новой книги."""
        self.session.add(book)
        self.session.commit()
        print(f"Книга '{book.title}' добавлена.")

    def get_books_by_author(self, author_id: int):
        """Получение всех книг автора по его ID."""
        books = self.session.query(Book).filter(Book.author_id == author_id).all()
        return books

    def delete_book(self, book_id: int):
        """Удаление книги по её ID."""
        book = self.session.query(Book).get(book_id)
        if book:
            self.session.delete(book)
            self.session.commit()
            print(f"Книга с ID {book_id} удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")