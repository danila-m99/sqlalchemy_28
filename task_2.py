from models import User
from sqlalchemy.exc import IntegrityError
from main import session

def add_users_with_transaction():
    try:
        with session.begin():
            user1 = User(username="user1", email="user1@example.com")
            user2 = User(username="user2", email="user2@example.com")
            session.add_all([user1, user2])

            # Имитация ошибки
            user3 = User(username="user3", email="user1@example.com")
            session.add(user3)

    except IntegrityError as e:
        session.rollback()
        print("Ошибка при добавлении пользователей. Все изменения откатились.")
    else:
        print("Все пользователи добавлены успешно.")

if __name__ == "__main__":
    print("\nТранзакция с пользователями:")
    add_users_with_transaction()

    # Проверка содержимого таблицы users
    users = session.query(User).all()
    print("\nПользователи в базе данных:")
    for user in users:
        print(f"- {user.username}: {user.email}")