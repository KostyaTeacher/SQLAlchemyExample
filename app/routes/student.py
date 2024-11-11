from flask import redirect, render_template, request, Blueprint, url_for

from ..db import (
    Session,
    Student,
    Group,
)
from sqlalchemy import select
from datetime import datetime

students_blueprint = Blueprint("students", __name__, url_prefix="/students")


def get_age(born):
    dob = datetime.strptime(born, "%Y-%m-%d")
    current_date = datetime.now()
    age = (
        current_date.year
        - dob.year
        - ((current_date.month, current_date.day) < (dob.month, dob.day))
    )
    return age
    #


@students_blueprint.post("/")
def add_item():
    with Session() as session:
        item_groups = (
            session.query(Group)
            .where(Group.id.in_(request.form.getlist("groups")))
            .all()
        )
        item = Student(
            name=request.form.get("name"),
            surname=request.form.get("surname"),
            age=get_age(request.form.get("birth_date")),
            address=request.form.get("address"),
            groups=item_groups,
        )
        session.add(item)
        session.commit()
        return redirect(url_for("students.management"))


@students_blueprint.get("/")
def management():
    with Session() as session:

        data = session.query(Student).all()
        groups = session.query(Group).all()
    return render_template(
        "student/management.html",
        iterable=data,
        groups=groups,
    )


@students_blueprint.get("/<int:id>")
def get_item(id):
    with Session() as session:
        data = session.scalars(select(Student).where(Student.id == id)).first()
        print(data)

    return render_template("main.html", content=data)
