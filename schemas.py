from marshmallow import Schema, fields

class PlainStudant(Schema):
  id = fields.Str(dump_only=True)
  name = fields.Str(required=True)
  birthdate = fields.Str(required=True)
  status = fields.Bool(required=True)
  enrollment = fields.Str(required=True)
  
class StudantUpdateSchema(Schema):
  name = fields.Str(required=True)
  status = fields.Bool(required=True)
  