

from flask import Flask, request, jsonify
import requests
import json
import jwt
import datetime

app = Flask(__name__)

# Configurações do FireHydrant e Zoom
FIREHYDRANT_API_URL = 'https://api.firehydrant.io/v1/incidents'
FIREHYDRANT_API_KEY = 'YOUR_FIREHYDRANT_API_KEY'
ZOOM_API_KEY = 'YOUR_ZOOM_API_KEY'
ZOOM_API_SECRET = 'YOUR_ZOOM_API_SECRET'

def generate_jwt():
    payload = {
        'iss': ZOOM_API_KEY,
        'exp': datetime.datetime.now() + datetime.timedelta(minutes=5)
    }
    return jwt.encode(payload, ZOOM_API_SECRET, algorithm='HS256')

@app.route('/slack-webhook', methods=['POST'])
def slack_webhook():
    data = request.json
    action = data.get('actions', [{}])[0].get('value')

    if action == 'create_incident':
        # Lógica para criar um incidente no FireHydrant
        # [Sua lógica aqui]
        return jsonify({"text": "Incidente criado."})

    elif action == 'start_zoom_call':
        jwt_token = generate_jwt()
        zoom_meeting_data = {
            "topic": "Reunião de Incidente",
            "type": 1,  # 1 para reunião instantânea
            "settings": {
                "host_video": True,
                "participant_video": True,
                "join_before_host": True,
                "mute_upon_entry": True
            }
        }

        # Criar a reunião no Zoom
        response = requests.post(
            'https://api.zoom.us/v2/users/me/meetings',
            headers={'Authorization': f'Bearer {jwt_token}'},
            json=zoom_meeting_data
        )

        if response.status_code == 201:
            meeting_info = response.json()
            join_url = meeting_info['join_url']
            return jsonify({"text": f"Chamada iniciada! Você pode participar aqui: {join_url}"})
        else:
            return jsonify({"text": "Erro ao iniciar a chamada no Zoom."}), 500

    return jsonify({"text": "Ação não reconhecida."}), 400

@app.route('/send_button', methods=['POST'])
def send_button():
    with open('slack-button.json') as f:
        button_payload = json.load(f)

    slack_webhook_url = 'https://hooks.slack.com/services/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'
    response = requests.post(slack_webhook_url, json=button_payload)

    if response.status_code == 200:
        return jsonify({"text": "Botão enviado com sucesso!"})
    else:
        return jsonify({"text": "Erro ao enviar o botão."}), 500

if __name__ == '__main__':
    app.run(port=3000, debug= True)

