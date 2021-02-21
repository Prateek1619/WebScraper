from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import json, os
from .links import *
from News_app.config import Config



app = Flask(__name__)
api = Api(app)

app.config.from_object(Config)
db = SQLAlchemy(app)

from News_app.models import *
@app.before_first_request
def create_tables():
    db.create_all()

from News_app.routes import News_t
app.register_blueprint(News_t)