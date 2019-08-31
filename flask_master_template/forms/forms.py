from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, \
    BooleanField, SubmitField, SelectField, PasswordField, \
    FileField
from wtforms.validators import DataRequired, Length


class LoginForms(FlaskForm):
    username = StringField('Username', validators=[Length(min=0, max=16)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class ExampleForm(FlaskForm):
    string = StringField('String', validators=[Length(min=0, max=16)])
    password = PasswordField('Password', validators=[])
    floats = FloatField('Float', validators=[])
    booleans = BooleanField('Boolean', validators=[])
    selects = SelectField(u'Select', choices=[('one', 'One'),
                                              ('two', 'Two'),
                                              ('three', 'Three')])
    files = FileField('File', validators=[])
    dates = DateField('Date', validators=[])
    submit = SubmitField('Login')
