from db import db

class NoteModel(db.Model):
	__tablename__ = 'studants'
	__table_args__ = {'sqlite_autoincrement': True}
	id = db.Column(db.Integer, primary_key=True)
	nota_1 = db.Column(db.Float, nullable=True)
	nota_2 = db.Column(db.Float, nullable=True)
	nota_final = db.Column(db.Float, nullable=True)
	