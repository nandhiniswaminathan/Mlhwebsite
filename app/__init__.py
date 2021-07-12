import os
import flask
from flask import Flask, render_template
from . import db
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
    db.init_app(app)

    @app.route('/')
    def index():
        user = {'username': 'Nandhini'}
        return render_template('home.html', title='Home', user=user)

    @app.route('/health', methods=['GET'])
    def health():
        return "200"

    @app.route('/register', methods=('GET', 'POST'))
    def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif UserModel.query.filter_by(username=username).first() is not None:
            error = f"User {username} is already registered."

        if error is None:
            new_user = UserModel(username, generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return f"User {username} created successfully"
        else:
            return error, 418

    return render_template("register.html")


    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            error = None
            user = UserModel.query.filter_by(username=username).first()

            if user is None:
                error = "Incorrect username."
            elif not check_password_hash(user.password, password):
                error = "Incorrect password."

            if error is None:
                return "Login Successful", 200
            else:
                return error, 418
    return render_template("login.html")

    return app
app = create_app()
