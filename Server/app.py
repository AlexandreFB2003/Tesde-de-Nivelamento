from flask import Flask
from config import Config
from route import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, port=Config.SERVER_PORT)
