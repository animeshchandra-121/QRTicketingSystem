from rest_framework import serializers
from .models import User, MessProfile, MessVisit, OneTimeToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class MessProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = MessProfile
        fields = ['user', 'is_day_scholar', 'amt_paid']

class MessVisitSerializer(serializers.ModelSerializer):
    user = MessProfileSerializer(read_only= True)

    class Meta:
        model = MessVisit
        fields = ['user', 'session_id', 'entry_scanned_at', 'exit_scanned_at']

class OneTimeTokenSerializer(serializers.ModelSerializer):
    user = MessProfileSerializer(read_only = True)
    visit = MessVisitSerializer(read_only = True)
    class Meta:
        model = OneTimeToken
        fields = ['user', 'visit', 'token_type', 'token', 'device_id', 'gate_id', 'used', 'expires_at']
