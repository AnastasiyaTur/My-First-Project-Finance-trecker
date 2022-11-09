from database import db_session
from flask import Blueprint, flash, redirect, render_template, request, url_for
from webapp.category.forms import CreateCategory
from webapp.category.models import СategoryName

blueprint = Blueprint('category', __name__, url_prefix='/categories')


@blueprint.route('/category_income')
def category_income():
    # Page with all income categories
    categories_income_list = СategoryName.query.filter_by(budget_type_id=2).all()
    return render_template('category/category_income.html',
                           categories_income_list=categories_income_list)


@blueprint.route('/category_expenses')
def category_expenses():
    # Page with all categories of expenses
    categories_expenses_list = СategoryName.query.filter_by(budget_type_id=1).all()
    return render_template(
        'category/category_expenses.html',
        categories_expenses_list=categories_expenses_list)


@blueprint.route('/create_category')
def create_category():
    # Page with a form for creating a new category
    title = "Create category"
    create_category_form = CreateCategory()
    return render_template('category/create_category.html', page_title=title,
                           form=create_category_form)


@blueprint.route("/process_create_category", methods=['GET', 'POST'])
def process_create_category():
    # Process of creating a new category with a record in the database
    form = CreateCategory()
    category = СategoryName.query.filter(СategoryName.name == form.category_name.data).first()
    print(category)
    if category is None:
        type = request.form['inlineRadioOptions']
        if type == '1':
            category = СategoryName(name=form.category_name.data, budget_type_id=type)
            db_session.add(category)
            db_session.commit()
            flash('Create category successfully')
            return redirect(url_for('category.category_expenses'))
        else:
            category = СategoryName(name=form.category_name.data, budget_type_id=type)
            db_session.add(category)
            db_session.commit()
            flash('Create category successfully')
            return redirect(url_for('category.category_income'))

    flash('An error has occurred. Data not saved')
    return redirect(url_for('category.create_category'))


@blueprint.route('/category/<int:id>/delete', methods=['GET', 'POST'])
def category_delete(id):
    # Process of deleting a category
    category = СategoryName.query.filter_by(id=id).first()
    if category.budget_type_id == 1:
        try:
            db_session.delete(category)
            db_session.commit()
            flash('Delete category successfully')
            return redirect(url_for('category.category_expenses'))
        except Exception as e:
            print(f'Error {e}')
            flash('An error has occurred. The category has not been removed.')
            return redirect(url_for('category.category_expenses'))
    else:
        try:
            db_session.delete(category)
            db_session.commit()
            flash('Delete category successfully')
            return redirect(url_for('category.category_income'))
        except Exception as e:
            print(f'Error {e}')
            flash('An error has occurred. The category has not been removed.')
            return redirect(url_for('category.category_income'))


@blueprint.route("/category/<int:id>/edit", methods=['GET', 'POST'])
def category_edit(id):
    # Process of changing category data
    category = СategoryName.query.get(id)
    if request.method == "POST":
        category.name = request.form['name']
        category.budget_type_id = request.form['inlineRadioOptions']
        if category.budget_type_id == '1':
            try:
                db_session.commit()
                return redirect(url_for('category.category_expenses'))
            except Exception as e:
                print(f"Error {e}")
        else:
            try:
                db_session.commit()
                return redirect(url_for('category.category_income'))
            except Exception as e:
                print(f"Error {e}")
    else:
        return render_template("category/edit_category.html",
                               category=category)
