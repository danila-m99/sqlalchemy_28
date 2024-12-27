from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"DATABASE_URL из .env: {DATABASE_URL}")

# Создаём движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Фабрика сессий
SessionFactory = sessionmaker(bind=engine)