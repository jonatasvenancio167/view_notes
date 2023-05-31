from marshmallow import Schema, fields

class PlainStudant(Schema):
  id = fields.Int(required=True)
  cpf = fields.Str(required=True)
  name = fields.Str(required=True)
  birthdate = fields.Str(required=True)
  sex = fields.Str(required=True)
  age = fields.Str(required=True)
  
class PlainNoteSchema(Schema):
  id = fields.Int(dump_only=True)
  note_1 = fields.Float(required=True)
  note_2 = fields.Float(required=False)
  finally_note = fields.Float(required=False)

class StudantUpdateSchema(Schema):
  name = fields.Str(required=True)
  
class StudantSchema(PlainStudant):
  notes = fields.List(fields.Nested(lambda: PlainNoteSchema()), dump_only=True)
  
class NoteSchema(PlainNoteSchema):
  studant_id = fields.Int(required=True, load_only=True)
  studant = fields.Nested(lambda: PlainNoteSchema(), dump_only=True)
