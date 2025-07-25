from rest_framework import serializers
from .models import Promotion
from apps.movies.models import Movie
from django.utils import timezone

class PromotionSerializer(serializers.ModelSerializer):
    applicable_movies = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Movie.objects.all(), required=False
    )

    class Meta:
        model = Promotion
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'used_count', 'created_by')

    def validate_discount_value(self, value):
        if value <= 0:
            raise serializers.ValidationError("El valor del descuento debe ser mayor que cero.")
        return value

    def validate_max_discount_amount(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("El monto máximo de descuento debe ser mayor que cero.")
        return value

    def validate_usage_limit(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("El límite de uso debe ser mayor que cero.")
        return value

    def validate_valid_weekdays(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise serializers.ValidationError("Los días válidos deben ser una lista.")
            for day in value:
                if day not in range(0, 7):
                    raise serializers.ValidationError("Los días válidos deben estar entre 0 (lunes) y 6 (domingo).")
        return value

    def validate(self, data):
        start = data.get('start_date') or self.instance.start_date if self.instance else None
        end = data.get('end_date') or self.instance.end_date if self.instance else None
        usage_limit = data.get('usage_limit') or self.instance.usage_limit if self.instance else None
        used_count = data.get('used_count') or self.instance.used_count if self.instance else 0

        if start and end and start > end:
            raise serializers.ValidationError("La fecha de inicio no puede ser posterior a la fecha de término.")

        if usage_limit is not None and used_count > usage_limit:
            raise serializers.ValidationError("El número de usos ya excede el límite establecido.")

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        return super().create(validated_data)
