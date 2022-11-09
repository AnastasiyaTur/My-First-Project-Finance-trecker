from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired


class CreateAccount(FlaskForm):
    # Create a new account
    account_name = StringField('Account name', validators=[DataRequired()],
                               render_kw={"class": "form-control"})
    amount = FloatField('Amount', validators=[DataRequired()],
                        render_kw={"class": "form-control"})
    submit = SubmitField('Add', render_kw={"class": "btn btn-primary"})
