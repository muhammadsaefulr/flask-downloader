from flask import Flask
from flask_cors import CORS
from middleware.login import login_procces
from controller.instaurl import app_flask_insta
from controller.youtubeurl import app_flask_yt
from middleware.auth import check_access
from middleware.register import registers_account

app = Flask(__name__)
CORS(app, origins='*')

app.register_blueprint(registers_account, url_prefix='/api/v1')
app.register_blueprint(login_procces, url_prefix='/api/v1')
app.register_blueprint(app_flask_insta, url_prefix='/api/v1')
app.register_blueprint(app_flask_yt, url_prefix='/api/v1')

if __name__ == "__main__":
    app.run(debug=True)
