from db import db
from sqlalchemy import text

class NoteModel(db.Model):
  __tablename__ = 'notes'
  __table_args__ = {'sqlite_autoincrement': True}

  id = db.Column(db.Integer, unique=True, primary_key=True)
  note_1 = db.Column(db.Float(precision=2), default=0.0)
  note_2 = db.Column(db.Float(precision=2), default=0.0)
  finally_note = db.Column(db.Float(precision=2), default=0.0)
  
  studant_id = db.Column(
		db.Integer, db.ForeignKey("studants.id"), nullable=False
  )
  studant = db.relationship("StudantModel", back_populates="notes")
  
  def serialize_with_student(self):
    return {
      "id": self.id,
      "note_1": self.note_1,
      "note_2": self.note_2,
      "finally_note": self.finally_note,
    }
