from app import db

class Studants(db.Model):
	__tablename__ = 'studants'
	__table_args__ = {'sqlite_autoincrement': True}
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	age = db.Column(db.Integer)
	status = db.Column(db.Boolean)
	enrollment = db.Column(db.string(13))
	
	def __init__(self, name, age, status, enrollment):
		self.name = name
		self.age = age
		self.status = status
		self.enrollment = enrollment
	
	def json(self):
		return {
			'name': self.name,
			'age': self.age,
			'status': self.status,
			'enrollment': self.enrollment
		}
  
	def save_studant(self):
		try:
			db.session.add(self)
			db.session.commit()
		except Exception as e:
			print(e)