#!/usr/bin/env python3
""" Flask Blueprint for implementing FAQ Bot's logic """
from . import app_blueprints
from flask import jsonify, render_template, request


@app_blueprints.route('/home')
def home():
    """ Renders the index.html template """
    return render_template('index.html')


@app_blueprints.route('/bot', methods=['POST'])
def bot():
    """
    
    Handles incoming user input, processes it with FAQ bot logic,
    and returns a JSON response with the bot's reply.

    """
    user_input = request.json.get('user_input')

    bot_response = "Thanks for reaching out!"

    return jsonify({'bot_response': bot_response})
