#!/usr/bin/env python3
""" Flask Blueprint for implementing FAQ Bot's logic """
from . import app_blueprints
from flask import jsonify, request
from models.bot_manager import RuleBasedBot, Admin
from config import smtp_config_instance
from app import celery  # Import Celery instance

bot_instance = RuleBasedBot()
admin_instance = Admin(bot_instance)

@celery.task
def process_user_input(user_input, admin_instance, smtp_config):
    return bot_instance.respond(
        user_input, admin_instance,
        smtp_config.smtp_server,
        smtp_config.smtp_port,
        smtp_config.sender_email,
        smtp_config.sender_password,
        smtp_config.recipient_email
    )

@app_blueprints.route('/bot', methods=['POST'])
def bot():
    user_input = request.json.get('user_input')

    # Call the Celery task asynchronously
    task = process_user_input.delay(user_input, admin_instance, smtp_config_instance)

    return jsonify({'task_id': task.id}), 202
