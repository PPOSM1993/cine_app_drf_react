# fidelity/serializers.py

from rest_framework import serializers
from .models import FidelityAccount, Reward, FidelityTransaction

# --- FidelityAccount ---
class FidelityAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FidelityAccount
        fields = '__all__'
        read_only_fields = ['user', 'updated_at']


# --- Reward ---
class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'
        read_only_fields = ['created_at']

    def validate_points_required(self, value):
        if value < 0:
            raise serializers.ValidationError("Los puntos requeridos no pueden ser negativos.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser negativo.")
        return value


# --- FidelityTransaction ---
class FidelityTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FidelityTransaction
        fields = '__all__'
        read_only_fields = ['created_at']

    def validate_points(self, value):
        if value <= 0:
            raise serializers.ValidationError("Los puntos deben ser mayores a cero.")
        return value

    def validate(self, data):
        if data['type'] == 'redeem' and not data.get('reward'):
            raise serializers.ValidationError("Debe especificar una recompensa al canjear.")
        return data
