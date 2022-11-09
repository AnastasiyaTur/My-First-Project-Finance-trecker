from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import DataRequired


class CreateCategory(FlaskForm):
    # Create a new category
    category_name = StringField('Category name', validators=[DataRequired()],
                                render_kw={"class": "form-control"})
    budget_type = RadioField('Budget type',
                             choices=[(1, 'Expenses'), (2, 'Income')])
    submit = SubmitField('Add', render_kw={"class": "btn btn-primary"})
