from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp
from wtforms.fields.html5 import DateField


class PostForm(FlaskForm):
    title = StringField(
        'Titre',
        validators=[
            DataRequired(),
            Length(
                min=2,
                max=100,
                message='La longueur minimum est 2 carateres, '
                'et le maximum est 100 caracteres.')])

    content = TextAreaField(
        'Contenu',
        validators=[
            DataRequired(),
            Length(
                min=2,
                max=500,
                message='La longueur minimum est 2 carateres, '
                'et le maximum est 500 caracteres.')])

    date = StringField(
        'Date parution',
        validators=[
            DataRequired(),
            Regexp(
                r'^(?:[1-9]\d{3}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|'
                r'1\d|2[0-8])|(?:0[13-9]|1[0-2])-(?:29|30)|(?:0[13578]|'
                r'1[02])-31)|(?:[1-9]\d(?:0[48]|[2468][048]|[13579][26])|'
                r'(?:[2468][048]|[13579][26])00)-02-29) (?:[01]\d|'
                r'2[0-3]):[0-5]\d:[0-5]\d\.[0-9]\d{2}$',
                message="Date invalide, "
                "le format est YYYY-MM-JJ HH:mm:ss.sss")])

    auteur = StringField(
        'Auteur',
        validators=[
            DataRequired(),
            Length(
                min=2,
                max=100,
                message='La longueur minimum est 2 carateres, '
                'et le maximum est 100 caracteres.')])

    identifiant = StringField(
        'Identifiant', validators=[
            DataRequired(), Length(
                min=2, max=50, message='La longueur minimum est 2 carateres, '
                'et le maximum est 100 caracteres.'),
            Regexp(
                r'^\w+$',
                message='Seul les caracteres '
                'alphanumeriques sont autorises.')])

    submit = SubmitField('Poster')


class ModifyPostForm(FlaskForm):
    title = StringField(
        'Titre',
        validators=[
            DataRequired(),
            Length(
                min=2,
                max=100,
                message='La longueur minimum est 2 carateres, '
                'et le maximum est 100 caracteres.')])

    content = TextAreaField(
        'Contenu',
        validators=[
            DataRequired(),
            Length(
                min=2,
                max=500,
                message='La longueur minimum est 2 carateres, '
                'et le maximum est 500 caracteres.')])

    submit = SubmitField('Poster')
