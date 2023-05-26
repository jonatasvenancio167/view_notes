from db import db

class StudantModel(db.Model):
	__tablename__ = 'studants'
	__table_args__ = {'sqlite_autoincrement': True}
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	birthdate = db.Column(db.String, nullable=False)
	status = db.Column(db.Boolean, nullable=False)
	enrollment = db.Column(db.String(13), unique=True, nullable=False)
	
