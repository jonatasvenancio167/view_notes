from flask import Flask 
from flask_restful import SQLAlchemy
import sqlite3

app = Flask(__name__):
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studant0.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
db = SQLAlchemy(app)
api = Api(app)

from app.models.studants import Studants
with app.app_context():
    db.create_all()
  
from app.resources.result_studants import Index, StudantCreate, StudantSearch
api.add_resource(Index, '/')
api.add_resource(SurvivorCreate, '/criar')
api.add_resource(SurvivorsSearch, '/buscar_todos')
                 
