from flask import Flask
from config import Config
from .api.routes import api_bp
from .jobs import scheduler

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.register_blueprint(api_bp)

    scheduler.init_app(app)
    scheduler.start()

    return app
