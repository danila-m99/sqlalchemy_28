from sqlalchemy import create_engine
from models import Base
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()
print(f"DATABASE_URL из .env: {os.getenv('DATABASE_URL')}")

# Получаем строку подключения
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("Строка подключения к базе данных не найдена в .env файле")

# Создаём движок и создаём таблицы
engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    print("Создание таблиц в базе данных...")
    Base.metadata.create_all(engine)
    print("Таблицы успешно созданы!")