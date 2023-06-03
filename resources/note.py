from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import NoteModel
from schemas import PlainNoteSchema, NoteSchema

blp = Blueprint("Notes", "notes", description="Operations on notes")

@blp.route("/note/<string:note_id>")
class Note(MethodView):
  @blp.response(200, PlainNoteSchema)
  def get(self, note_id):
    note = NoteModel.query.get_or_404(note_id)
    return note
  
  def delete(self, note_id):
    note = NoteModel.query.filter_by(id=note_id).first_or_404()
    db.session.delete(note)
    db.session.commit()
    return { "message": "Note deleted." }
  
  @blp.response(200, PlainNoteSchema)
  def put(self, note_data, note_id):
    avaliation = NoteModel.query.get(note_id)
    
    if avaliation:
      avaliation.note_1 = note_data["note_1"]
      avaliation.note_2 = note_data["note_2"]
      avaliation.finally_note = note_data["finally_note"]
    else:
      avaliation = NoteModel(id=note_id, **note_data)
      
    db.session.add(avaliation)
    db.session.commit()
    
    return avaliation

@blp.route("/note")
class NoteList(MethodView):
  @blp.response(200, PlainNoteSchema(many=True))
  def get(self):
    notes = NoteModel.query.all()
    for note in notes:
      print(note.studant)
    
    return notes
    
  @blp.arguments(NoteSchema)
  @blp.response(201, NoteSchema)
  def post(self, note_data):
    note = NoteModel(**note_data)

    try:
      db.session.add(note)
      db.session.commit()
    except SQLAlchemyError as e:
      abort(500, message=f"An error occurred while inserting the note {str(e)}")
      db.session.rollback()
    
    return note
