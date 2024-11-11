from flask import render_template, request, redirect, url_for  # Blueprint,


from ..db import (
    Session,
    Group,
)
from sqlalchemy import select
from .. import app


# groups_blueprint = Blueprint("groups", __name__, url_prefix="/groups")


@app.post("/groups/")
def add_groups_item():
    with Session() as session:
        session.add(Group(name=request.form.get("name")))
        session.commit()
        return redirect(url_for("groups_management"))


@app.get("/groups/")
def groups_management():
    with Session() as session:
        return render_template(
            "group/management.html",
            iterable=session.query(Group).all(),
        )


@app.get("/groups/<int:id>")
def get_groups_item(id):
    with Session() as session:
        data = session.scalars(select(Group).where(Group.id == id)).first()
        print(data)

    return render_template("main.html", content=data)
