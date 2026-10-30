
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Book


class BookRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_book(self, title: str, author_id: int):
        book = Book(title=title, author_id=author_id)
        self.session.add(book)
        self.session.commit()
        self.session.refresh(book)
        return book

    def get_all_books(self):
        return self.session.scalars(select(Book)).all()

    def get_book_by_id(self, book_id: int):
        return self.session.get(Book, book_id)

    def delete_book(self, book_id: int):
        book = self.get_book_by_id(book_id)

        if book is None:
            return False

        self.session.delete(book)
        self.session.commit()
        return True
