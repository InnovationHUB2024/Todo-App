# core/tokens.py (for Django 4.0+)
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return f"{user.pk}{timestamp}{user.profile.is_verified}"

account_activation_token = AccountActivationTokenGenerator()
