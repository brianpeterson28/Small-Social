#from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                                Length, EqualTo)

from models import User

rf_message = ("Username should be one word, letters, numbers, and underscores "
              "only.")
pw_message = ("Passwords must match.")

def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with that name already exists.')

def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that e-mail already exists.')

class RegisterForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(),
                                        Regexp(r'^[a-zA-Z0-9_]+$', 
                                        message=rf_message),
                                        name_exists]
                            )

    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email(),
                                    email_exists
                                    ])

    password = PasswordField('Password',
                              validators=[DataRequired(),
                                          Length(min=2),
                                          EqualTo('password2', 
                                                   message=pw_message)
                                          ])

    password2 = PasswordField('Confirm Password',
                               validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class PostForm(FlaskForm):
    content = TextAreaField("What's up?", validators=[DataRequired()])


