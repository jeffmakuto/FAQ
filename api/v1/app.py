from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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

