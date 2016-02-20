from flask.ext.wtf import Form
from wtforms.fields import TextField, BooleanField,StringField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
