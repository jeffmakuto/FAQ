#!/usr/bin/env python3
"""
Module description: This module defines routes and socket events for a Flask application.

It includes route for handling bot-related requests through WebSocket.

Dependencies:
- flask_socketio
- flask
- models.bot_manager.RuleBasedBot
- models.bot_manager.Admin
- config.smtp_config_instance
"""
from flask_socketio import emit
from . import app_blueprints
from flask import jsonify, render_template, request
from models.bot_manager import RuleBasedBot, Admin
from config import smtp_config_instance
from .. import socketio

# Initialize instances
bot_instance = RuleBasedBot()
admin_instance = Admin(bot_instance)

@socketio.on('connect')
def handle_connect():
    """
    Socket event handler: Triggered when a client connects.
    """
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    """
    Socket event handler: Triggered when a client disconnects.
    """
    print('Client disconnected')

@app_blueprints.route('/bot', methods=['POST'])
def bot():
    """
    Route: /bot
    Method: POST
    Parameters: JSON data containing 'user_input'.
    Returns: JSON response with the bot's response.
    """
    user_input = request.json.get('user_input')
    bot_response = bot_instance.respond(
        user_input,
        admin_instance,
        smtp_config_instance.smtp_server,
        smtp_config_instance.smtp_port,
        smtp_config_instance.sender_email,
        smtp_config_instance.sender_password,
        smtp_config_instance.recipient_email
    )

    emit('bot_response', {'bot_response': bot_response}, broadcast=True)
    return jsonify({'bot_response': bot_response})
