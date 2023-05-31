from db import db

class StudantModel(db.Model):
	__tablename__ = 'studants'
	__table_args__ = {'sqlite_autoincrement': True}
 
	id = db.Column(db.Integer, unique=True, nullable=False)
	cpf = db.Column(db.String, unique=True, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	birthdate = db.Column(db.String, nullable=False)
	sex = db.Column(db.String, nullable=False)
	age = db.Column(db.String, nullable=False)
 
	notes = db.relationship("NoteModel", back_populates="studant")
