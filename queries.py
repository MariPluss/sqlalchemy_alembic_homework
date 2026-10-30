
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database import SessionLocal
from models import Author

with SessionLocal() as session:
    print("\n=== Обычная загрузка ===")

    authors = session.scalars(select(Author)).all()

    for author in authors:
        print(f"Автор: {author.name}")
        for book in author.books:
            print(f"  Книга: {book.title}")

with SessionLocal() as session:
    print("\n=== Оптимизированная загрузка ===")

    authors = session.scalars(
        select(Author).options(selectinload(Author.books))
    ).all()

    for author in authors:
        print(f"Автор: {author.name}")
        for book in author.books:
            print(f"  Книга: {book.title}")
