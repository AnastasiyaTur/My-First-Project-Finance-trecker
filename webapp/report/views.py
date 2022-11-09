from flask import Blueprint, redirect, render_template, url_for
from webapp.report.reports import (pie_chart_expenses, pie_chart_income,
                                   bar_chart_expenses, bar_chart_income)

blueprint = Blueprint('report', __name__, url_prefix='/reports')


@blueprint.route('/reports')
def reports():
    # Page with budget reports
    title = "Reports"
    return render_template('report/reports.html', page_title=title)


@blueprint.route('/expenses_pie_chart', methods=['GET', 'POST'])
def expenses_pie_chart():
    # Create of a pie chart of expenses
    try:
        pie_chart_expenses()
        return redirect(url_for('report.reports'))
    except Exception as e:
        print(f"Error {e}")
        return redirect(url_for('report.reports'))


@blueprint.route('/income_pie_chart', methods=['GET', 'POST'])
def income_pie_chart():
    # Create of a pie chart of income
    try:
        pie_chart_income()
        return redirect(url_for('report.reports'))
    except Exception as e:
        print(f"Error {e}")
        return redirect(url_for('report.reports'))


@blueprint.route('/expenses_bar_chart', methods=['GET', 'POST'])
def expenses_bar_chart():
    # Create of a bar chart of expenses
    try:
        bar_chart_expenses()
        return redirect(url_for('report.reports'))
    except Exception as e:
        print(f"Error {e}")
        return redirect(url_for('report.reports'))


@blueprint.route('/income_bar_chart', methods=['GET', 'POST'])
def income_bar_chart():
    # Create of a bar chart of income
    try:
        bar_chart_income()
        return redirect(url_for('report.reports'))
    except Exception as e:
        print(f"Error {e}")
        return redirect(url_for('report.reports'))
