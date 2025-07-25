from rest_framework import serializers
from .models import SupportCategory, SupportTicket

class SupportCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportCategory
        fields = '__all__'

class SupportTicketSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = SupportTicket
        fields = [
            'id', 'subject', 'message', 'user', 'user_email',
            'category', 'category_name', 'status', 'priority',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate_subject(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El asunto debe tener al menos 5 caracteres.")
        return value

    def validate_message(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("El mensaje debe ser más detallado.")
        return value

    def validate(self, data):
        if data.get('status') == 'closed' and not self.instance:
            raise serializers.ValidationError("No puedes crear un ticket cerrado desde el inicio.")
        return data

class SupportTicketListSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = SupportTicket
        fields = [
            'id', 'subject', 'user_email', 'category_name',
            'status', 'priority', 'created_at'
        ]

class SupportTicketDetailSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = SupportTicket
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
