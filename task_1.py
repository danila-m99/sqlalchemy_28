from models import Author, Book
from sqlalchemy.orm import joinedload
from main import session

def lazy_loading_example():
    authors = session.query(Author).all()
    for author in authors:
        print(f"Author: {author.name}")
        print("Books:")
        for book in author.books:
            print(f" - {book.title}")

def eager_loading_example():
    authors = session.query(Author).options(joinedload(Author.books)).all()
    for author in authors:
        print(f"Author: {author.name}")
        print("Books:")
        for book in author.books:
            print(f" - {book.title}")

if __name__ == "__main__":
    print("\nЛенивая загрузка:")
    lazy_loading_example()
    print("\nЖадная загрузка:")
    eager_loading_example()