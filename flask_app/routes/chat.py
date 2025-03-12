from flask import Blueprint, request, jsonify, current_app
import subprocess

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Mesaj gönderilmedi.'}), 400

    user_message = data['message']
    try:
        # Config'den model adı ve timeout değerlerini alıyoruz
        model_name = current_app.config.get("MODEL_NAME", "deepseek-r1:8b")
        timeout_val = current_app.config.get("MODEL_TIMEOUT", 30)
        process = subprocess.run(
            ['ollama', 'run', model_name],
            input=(user_message + "\n").encode('utf-8'),
            capture_output=True,
            timeout=timeout_val
        )
        if process.returncode != 0:
            return jsonify({
                'error': 'Model çalıştırılırken hata oluştu.',
                'details': process.stderr.decode('utf-8')
            }), 500

        response_text = process.stdout.decode('utf-8').strip()
        return jsonify({'response': response_text})
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Model çalıştırma süresi aşıldı.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500