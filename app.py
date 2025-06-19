from flask import Flask, request, jsonify
from chatbot import respond

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')

    if not message:
        return jsonify({'error': 'No message provided'}), 400

    response = respond(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
