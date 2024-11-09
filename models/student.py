from __future__ import annotations

from typing import (
    List,
    Optional,
)
from sqlalchemy import (
    ForeignKey,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from . import Base
from .associates import student_group_assoc_table
from .group import Group


class Student(Base):
    __tablename__ = "student"  # Ім'я таблиці в БД, може відрізнятися від моделі

    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[Optional[str]]  # Optional дає можливість не контролювати заповнення поля
    name: Mapped[str] = mapped_column(
        String(50)
    )  # Для поля типу str обов'язково потрібно вказувати максимальну довжину, якщо не Optional
    age: Mapped[int] = mapped_column()  # Для поля типу int ніяких обов'язкових агрументів немає
    address: Mapped[str] = mapped_column(String(250))

    # Встановлення відношення до іншої моделі через другорядну таблицю(ассоціація)
    groups: Mapped[List[Group]] = relationship(
        secondary=student_group_assoc_table,
    )
