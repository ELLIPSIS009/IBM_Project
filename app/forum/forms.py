from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    content = TextAreaField('Say something', validators=[DataRequired()])
    submit = SubmitField('Post')

class ThreadForm(PostForm):
    title = StringField('Title', validators=[DataRequired()])

class DeleteForm(FlaskForm):
    submit = SubmitField('Delete')
