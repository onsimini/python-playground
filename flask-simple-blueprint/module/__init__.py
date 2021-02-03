from flask import Flask

app = Flask(__name__)

from module.test_bp.test_bp import bp
app.register_blueprint(bp)
# app.add_url_rule('/', endpoint='index')
