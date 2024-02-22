#!/usr/bin/env python3
""" Module to generate key to be used in app.py """
import secrets


class SecretKeyGenerator:
    @staticmethod
    def generate_secret_key():
        """
        Generate a secure random secret key for Flask.
        """
        return secrets.token_hex(24)
