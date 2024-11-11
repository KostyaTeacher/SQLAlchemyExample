from flask import Flask
from .routes import (
    students_blueprint,
    default_blueprint,
    groups_blueprint,
)

app = Flask(__name__)

app.register_blueprint(default_blueprint)
app.register_blueprint(students_blueprint)
app.register_blueprint(groups_blueprint)
