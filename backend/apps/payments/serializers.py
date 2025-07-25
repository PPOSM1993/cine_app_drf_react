from rest_framework import serializers
from .models import Payment
from django.utils import timezone
import uuid

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'user',
            'ticket',
            'reservation',
            'amount',
            'method',
            'status',
            'transaction_code',
            'paid_at',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['transaction_code', 'status', 'paid_at', 'created_at', 'updated_at']

    def validate(self, data):
        ticket = data.get('ticket')
        reservation = data.get('reservation')

        if not ticket and not reservation:
            raise serializers.ValidationError("Debes asociar el pago a un ticket o una reserva.")
        
        if ticket and reservation:
            raise serializers.ValidationError("No puedes asociar un pago a un ticket y una reserva al mismo tiempo.")

        return data

    def create(self, validated_data):
        validated_data['transaction_code'] = str(uuid.uuid4())
        validated_data['status'] = 'completed'
        validated_data['paid_at'] = timezone.now()
        return super().create(validated_data)


class PaymentListSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Payment
        fields = [
            'id',
            'user_email',
            'amount',
            'method',
            'status',
            'transaction_code',
            'paid_at',
        ]


class PaymentDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    ticket = serializers.StringRelatedField()
    reservation = serializers.StringRelatedField()

    class Meta:
        model = Payment
        fields = '__all__'
