from __future__ import annotations

from typing import (
    List,
    Optional,
)
from sqlalchemy import (
    ForeignKey,
    String,
    Table,
    ForeignKey,
    Column,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from . import (
    Base
)
from .group import Group
from .associates import lesson_group_assoc_table


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150))
    groups: Mapped[List[Group]] = relationship(secondary=lesson_group_assoc_table)

    def __repr__(self):
        return f"<Lesson title:{self.title}>"

    def __str__(self):
        return self.title.capitalize()
