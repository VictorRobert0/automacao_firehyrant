

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL do FireHydrant API
FIREHYDRANT_API_URL = 'https://api.firehydrant.io/v1/incidents'
FIREHYDRANT_API_KEY = 'YOUR_FIREHYDRANT_API_KEY'  # Colocar chave da API do FireHydrant

@app.route('/slack-webhook', methods=['POST'])
def slack_webhook():
    # Obter os dados da solicitação do Slack
    data = request.json
    action = data.get('actions', [{}])[0].get('value')

    if action == 'create_incident':
        # Lógica para criar um incidente no FireHydrant
        try:
            # Exemplo de dados para o incidente
            incident_data = {
                "name": "Incidente de Teste",
                "description": "Este é um incidente criado via Slack.",
                "severity": "high"
            }

            headers = {
                'Authorization': f'Bearer {FIREHYDRANT_API_KEY}',
                'Content-Type': 'application/json'
            }

            response = requests.post(FIREHYDRANT_API_URL, json=incident_data, headers=headers)
            response.raise_for_status()  # Lança um erro se a requisição falhar

            incident_id = response.json().get('id')

            # Enviar uma mensagem de volta para o Slack
            return jsonify({
                "text": f"Incidente criado com sucesso: {incident_id}"
            })

        except requests.exceptions.RequestException as e:
            print(f"Erro ao criar incidente: {e}")
            return jsonify({"text": "Erro ao criar o incidente."}), 500

    return jsonify({"text": "Ação não reconhecida."}), 400

if __name__ == '__main__':
    app.run(port=3000)
