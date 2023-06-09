from decimal import Decimal
from db import db

class NoteModel(db.Model):
  __tablename__ = 'notes'
  __table_args__ = {'sqlite_autoincrement': True}

  id = db.Column(db.Integer, unique=True, primary_key=True)
  note_1 = db.Column(db.Float(precision=2), default=0.0)
  note_2 = db.Column(db.Float(precision=2), default=0.0)
  finally_note = db.Column(db.Float(precision=2), default=0.0)
  status = db.Column(db.String())
  
  studant_id = db.Column(
		db.Integer, db.ForeignKey("studants.id"), nullable=False
  )
  studant = db.relationship("StudantModel", back_populates="notes")
  
  def serialize_with_student(self):
    return {
      "id": self.id,
      "note_1": self.note_1,
      "note_2": self.note_2,
      "finally_note": self.calculate_final_grade(),
      "status" : self.final_result()
    }
  
  def calculate_final_grade(self):
    average = sum([Decimal(self.note_1), Decimal(self.note_2)]) / 2
    self.finally_note = round(average, 1)
    
    return self.finally_note
  
  def final_result(self):
    result = ""
    
    if self.note_1 > 0.0 and self.note_2 > 0.0 and self.finally_note >= 6:
      result = 'approved'
    else:
      result = 'reject'
      
    return result
    
