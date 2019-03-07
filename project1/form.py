
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email,EqualTo

class RegistrationForm(FlaskForm):
    username =StringField('Username',
                            validators=[DataRequired(),Length(min=2, max=20)])
    
    email =StringField('Email',
                            validators=[DataRequired(), Email()])
    
    password =PasswordField('Password',
                            validators =[DataRequired()])

    confirm_password =PasswordField('Confirm Password',
                            validators =[DataRequired(),EqualTo('password')])
    
    submit = SubmitField('SignUp')
    




class LoginForm(FlaskForm):
   
    
    username =StringField('Username',
                            validators=[DataRequired(), Email()])
    
    password =PasswordField('Password',
                            validators =[DataRequired()])
    submit = SubmitField('Login')

class ReviewForm(FlaskForm):
    review = StringField('Review',
                            validators =[DataRequired()])
    rating = IntegerField('Rating')

class SearchForm(FlaskForm):
    search = StringField('Search')
