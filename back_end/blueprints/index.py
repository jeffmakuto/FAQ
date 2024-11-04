#!/usr/bin/env python3
""" Flask Blueprint for implementing FAQ Bot's logic """
from . import app_blueprints
from flask import jsonify, render_template, request
from models.bot_manager import RuleBasedBot, Admin
from config import smtp_config_instance

bot_instance = RuleBasedBot()
admin_instance = Admin(bot_instance)


@app_blueprints.route('/home')
def home():
    """ Renders the index.html template """
    return render_template('index.html')

@app_blueprints.route('/bot', methods=['POST'])
def bot():
    try:
        user_input = request.json.get('user_input')
        if user_input is None:
            return jsonify({'error': 'User input is required'}), 400

        # Use SMTP configuration from smtp_config_instance
        bot_response = bot_instance.respond(
            user_input, admin_instance,
            smtp_config_instance.smtp_server,
            smtp_config_instance.smtp_port,
            smtp_config_instance.sender_email,
            smtp_config_instance.sender_password,
            smtp_config_instance.recipient_email
        )

        return jsonify({'bot_response': bot_response})

    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500
