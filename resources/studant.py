from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import StudantModel
from schemas import PlainStudant, StudantUpdateSchema

blp = Blueprint("Studants", "studants", description="Operations on studants")

@blp.route("/studant/<string:studant_id>")
class Studant(MethodView):
  @blp.response(200, PlainStudant)
  def get(self, studant_id):
    studant = StudantModel.query.get_or_404(studant_id)
    return studant
  
  def delete(self, studant_id):
    studant = StudantModel.query.get_or_404(studant_id)
    db.session.delete(studant)
    db.session.commit()
    return { "message": "Studant deleted." }
  
  @blp.arguments(StudantUpdateSchema)
  @blp.response(200, PlainStudant)
  def put(self, studant_data, studant_id):
    studant = StudantModel.query.get(studant_id)
    
    if studant:
      studant.name = studant_data["name"]
      studant.status = studant_data["status"]
    else:
      studant = StudantModel(id=studant_id, **studant_data)
      
    db.session.add(studant)
    db.session.commit()
    
    return studant

  @blp.route("/studant")
  class StudantList(MethodView):
    @blp.response(200, PlainStudant(many=True))
    def get(self):
      return StudantModel.query.all()
    
    @blp.arguments(PlainStudant)
    @blp.response(200, PlainStudant)
    def post(self, studant_data):
      studant = StudantModel(**studant_data)
      
      try:
        db.session.add(studant)
        db.session.commit()
      except SQLAlchemyError:
        abort(500, message="An error occurred while inserting the studant")
