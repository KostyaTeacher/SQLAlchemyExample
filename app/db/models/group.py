from sqlalchemy import (
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from . import (
    Base
)


class Group(Base):
    __tablename__ = "group"  # Ім'я таблиці в БД, може відрізнятися від моделі

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    def __repr__(self):
        return f"<Group name:{self.name}>"

