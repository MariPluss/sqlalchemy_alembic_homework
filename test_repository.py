
from database import SessionLocal
from repository import BookRepository

with SessionLocal() as session:
    repo = BookRepository(session)

    # 1. Добавляем новую книгу
    book = repo.add_book("Тестовая книга", 1)
    print(f"Книга добавлена: ID={book.id}, {book.title}")

    # 2. Получаем все книги
    books = repo.get_all_books()
    print(f"Всего книг: {len(books)}")

    # 3. Находим книгу по ID
    found = repo.get_book_by_id(book.id)
    print(f"Найдена книга: {found.title}")

    # 4. Удаляем тестовую книгу
    deleted = repo.delete_book(book.id)
    print(f"Книга удалена: {deleted}")
