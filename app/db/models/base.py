from sqlalchemy import (
    create_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,

)

# Створення двигуна, завдяки якому проводиться з'єднання з БД
engine = create_engine(
    "sqlite:///app.db",
    echo=True,  # завдяки цьому аргументу буде виведення запитів у термінал(sys.stdout)
)

# Створення конфігурації сесії на основі патерну Фабрика
Session = sessionmaker(bind=engine)


# Декларація базового класу для моделей
# Необхідно для реалізації відношень у ORM
class Base(DeclarativeBase):
    ...


def create_db():
    '''
    Ініціалізація метаданих,
    створює базу даних, якщо відсутня,
    створює таблиці на основі моделей(що спадкуються від Base),
    якщо жодної немає
    '''
    Base.metadata.create_all(engine)


def drop_db():
    '''
    Деструкція метаданих,
    видаляє базу даних, якщо така наявна,
    видаляє усі таблиці
    '''
    Base.metadata.drop_all(engine)

