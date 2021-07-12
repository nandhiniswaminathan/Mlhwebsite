import os
from flask import Flask, render_template
from . import db
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
    return app
app = create_app()
