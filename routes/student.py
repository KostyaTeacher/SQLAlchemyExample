from flask import render_template, request
from app import app
from models import (
    Session,
    Student,
    Group,
)
from sqlalchemy import select
from datetime import datetime


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


@app.route("/students", methods=["GET", "POST"])
def student_management():
    with Session() as session:
        if request.method == "POST":
            item_groups = session\
                .query(Group)\
                .where(
                    Group.id.in_(request.form.getlist("groups"))
                ).all()
            item = Student(
                name=request.form.get("name"),
                surname=request.form.get("surname"),
                age=get_age(request.form.get("birth_date")),
                address=request.form.get("address"),
                groups=item_groups,
            )
            session.add(item)
            session.commit()
        data = session.query(Student).all()
        groups = session.query(Group).all()
    return render_template(
        "student/management.html",
        iterable=data,
        groups=groups,
    )

@app.route("/students/<int:id>", methods=["GET"])
def student_get(id):
    with Session() as session:
        data = session.scalars(select(Student).where(Student.id == id)).first()
        print(data)

    return render_template("main.html", content=data)



