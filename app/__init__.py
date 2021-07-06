from flask import Flask, render_template
def create_app():
    app = Flask(__name__)
    @app.route('/')
    @app.route('/index')
    def index():
        user = {'username': 'Nandhini'}
        return render_template('home.html', title='Home', user=user)
    @app.route('/health', methods=['GET'])
    def health():
        return "200"
    return app
app = create_app()
