from flask import Flask
from app.routes import chatbot_routes

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(chatbot_routes)
    
    return app