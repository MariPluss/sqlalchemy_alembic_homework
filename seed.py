
from database import SessionLocal
from models import Author, Book

session = SessionLocal()

try:
    author1 = Author(name="Александр Пушкин")
    author2 = Author(name="Лев Толстой")

    author1.books = [
        Book(title="Капитанская дочка"),
        Book(title="Евгений Онегин"),
    ]

    author2.books = [
        Book(title="Война и мир"),
        Book(title="Анна Каренина"),
    ]

    session.add_all([author1, author2])
    session.commit()

    print("Авторы и книги успешно добавлены!")

finally:
    session.close()
