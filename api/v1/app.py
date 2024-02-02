from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

template_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'web_static', 'templates'))
app.template_folder = template_folder_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/bot', methods=['POST'])
def bot():
    user_input = request.json.get('user_input')

    # Replace the following with your actual FAQ bot logic
    bot_response = "Your response goes here."

    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)

