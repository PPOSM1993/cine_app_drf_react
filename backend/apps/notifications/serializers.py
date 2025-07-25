from rest_framework import serializers
from .models import Notification
from django.utils import timezone

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['created_at', 'sent_at', 'read_at', 'is_read']

    def validate(self, data):
        status = data.get('status', None)

        if status == 'sent' and not data.get('sent_at'):
            data['sent_at'] = timezone.now()
        elif status != 'sent' and data.get('sent_at'):
            raise serializers.ValidationError("Sent datetime should only be set if status is 'sent'.")

        if status == 'read' and not data.get('read_at'):
            data['read_at'] = timezone.now()
        elif status != 'read' and data.get('read_at'):
            raise serializers.ValidationError("Read datetime should only be set if status is 'read'.")

        return data

class NotificationListSerializer(serializers.ModelSerializer):
    is_read = serializers.BooleanField(read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'title', 'type', 'status', 'is_read', 'user_email', 'created_at']

class NotificationDetailSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Notification
        fields = [
            'id',
            'title',
            'message',
            'type',
            'status',
            'is_read',
            'payload',
            'user',
            'user_email',
            'created_at',
            'sent_at',
            'read_at',
        ]
        read_only_fields = ['created_at', 'sent_at', 'read_at', 'is_read', 'user_email']
