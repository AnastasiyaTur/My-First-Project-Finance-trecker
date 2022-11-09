from flask import Flask, render_template
from flask_login import LoginManager

from webapp.account.views import blueprint as account_blueprint
from webapp.budget.views import blueprint as budget_blueprint
from webapp.category.views import blueprint as category_blueprint
from webapp.report.views import blueprint as report_blueprint
from webapp.transaction.views import blueprint as transaction_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.user.models import User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(account_blueprint)
    app.register_blueprint(budget_blueprint)
    app.register_blueprint(category_blueprint)
    app.register_blueprint(report_blueprint)
    app.register_blueprint(transaction_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route("/")
    def index():
        title = "Finance trecker"
        return render_template('index.html', page_title=title)

    return app
