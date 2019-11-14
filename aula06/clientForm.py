from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Required

class ClientForm(FlaskForm):
    nome = StringField('nome:', validators=[Required()])
    endereço = StringField('endereço:', validators=[Required()])
    idade = StringField('idade:', validators=[Required()])
    submit = SubmitField('enviar')

