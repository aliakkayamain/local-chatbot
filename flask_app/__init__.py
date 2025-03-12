from flask import Flask
from flask_app.routes.chat import chat_bp
from flask_app.routes.index import index_bp
from flask_app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Ana sayfa route’u
    app.register_blueprint(index_bp)
    # Chat API endpoint’lerini /api altında topluyoruz
    app.register_blueprint(chat_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)