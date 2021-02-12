from flask import Flask

def create_app():
    app = Flask(__name__)

    from my_app.blueprints.views import view
    app.register_blueprint(view)

    return app
