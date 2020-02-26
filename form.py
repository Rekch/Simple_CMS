from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField

class PostForm(FlaskForm):
	title = StringField('Titre', validators=[DataRequired()])

	content = TextAreaField('Contenu', validators=[DataRequired()])

	date = DateField('Date parution', format='%Y-%m-%d', validators=[DataRequired()])

	auteur = StringField('Auteur', validators=[DataRequired(), Length(min=2, max=20)] )

	identifiant = StringField('Identifiant', validators=[DataRequired(), Length(min=2, max=20)])

	submit = SubmitField('Poster')

	

class ModifyPostForm(FlaskForm):
	title = StringField('Titre', validators=[DataRequired()])

	content = TextAreaField('Contenu', validators=[DataRequired()])

	submit = SubmitField('Poster')