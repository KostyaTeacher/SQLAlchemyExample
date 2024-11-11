from flask import render_template, request, Blueprint, redirect, url_for


from ..db import (
    Session,
    Group,
)
from sqlalchemy import select


groups_blueprint = Blueprint("groups", __name__, url_prefix="/groups")


@groups_blueprint.post("/")
def add_item():
    with Session() as session:
        session.add(Group(name=request.form.get("name")))
        session.commit()
        return redirect(url_for("groups.management"))


@groups_blueprint.get("/")
def management():
    with Session() as session:
        return render_template(
            "group/management.html",
            iterable=session.query(Group).all(),
        )


@groups_blueprint.get("/<int:id>")
def get_item(id):
    with Session() as session:
        data = session.scalars(select(Group).where(Group.id == id)).first()
        print(data)

    return render_template("main.html", content=data)
