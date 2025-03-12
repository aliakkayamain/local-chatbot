from flask import Blueprint

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return (
        "ALİ AKKAYA<br>"
        "Chatbox Servisi API'sine Hoşgeldiniz.<br>"
        "POST istekleri için /api/chat endpoint'ini kullanın."
    )