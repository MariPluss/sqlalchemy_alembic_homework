
from sqlalchemy.exc import IntegrityError

from database import SessionLocal
from models import User

with SessionLocal() as session:
    try:
        user1 = User(
            username="Anna",
            email="anna@example.com"
        )
        user2 = User(
            username="Ivan",
            email="ivan@example.com"
        )

        session.add_all([user1, user2])
        session.flush()
        raise IntegrityError(
            "Проверка отката транзакции",
           {},
             Exception("Тестовая ошибка")
        )
        session.commit()

        print("Пользователи успешно добавлены!")

    except IntegrityError:
        session.rollback()
        print("Ошибка! Транзакция отменена.")
