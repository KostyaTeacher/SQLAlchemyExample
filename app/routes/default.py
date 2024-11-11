from flask import render_template, Blueprint


default_blueprint = Blueprint("default", __name__, url_prefix="/")


@default_blueprint.get("/")
def main():
    return render_template("main.html")
