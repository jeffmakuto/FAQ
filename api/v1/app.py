from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

app.html_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'web_app', 'templates'))
app.static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'web_app', 'static'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/bot', methods=['POST'])
def bot():
    user_input = request.json.get('user_input')

    # Replace the following with your actual FAQ bot logic
    bot_response = "Thanks for reaching out!"

    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
