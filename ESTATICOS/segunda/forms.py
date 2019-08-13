from wtforms import Form
from wtforms import StringField
from wtforms import DateField
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms import SelectField

class GenerationForm(Form):
    firstname = StringField("Nombres")
    lastname = StringField("Apellido")
    number = StringField("Numero contacto")
    date = DateField("Fecha") 
    comment = TextAreaField("Comentario")
    button = SubmitField()
    