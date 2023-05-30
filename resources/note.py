from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import NoteModel
from schemas import PlainStudant, StudantUpdateSchema

blp = Blueprint("Notes", "notes", description="Operations on notes")

@blp.route("/note/<string:note_id>")
class Note(MethodView):
  @blp.response(200, PlainStudant)
  def get(self, note_id):
    note = NoteModel.query.get_or_404(note_id)
    return note
  
  @blp.arguments(StudantUpdateSchema)
  @blp.response(200, PlainStudant)
  def put(self, note_data, note_id):
    note = NoteModel.query.get(note_id)
    
    if note:
      note.nota_1 = note_data["nota_1"]
      note.nota_2 = note_data["nota_2"]
      note.nota_final = note_data["nota_final"]
    else:
      note = NoteModel(id=note_id, **note_data)
      
    db.session.add(note)
    db.session.commit()
    
    return note

@blp.route("/note")
class NoteList(MethodView):
  @blp.response(200, PlainStudant(many=True))
  def get(self):
    return NoteModel.query.all()
    
  @blp.arguments(PlainStudant)
  @blp.response(200, PlainStudant)
  def post(self, note_data):
    note = NoteModel(**note_data)
      
    try:
      db.session.add(note)
      db.session.commit()
    except SQLAlchemyError:
      abort(500, message="An error occurred while inserting the note")
