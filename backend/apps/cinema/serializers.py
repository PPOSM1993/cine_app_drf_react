from rest_framework import serializers
from .models import Cinema, Auditorium

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Cinema name must be at least 3 characters long.")
        return value

    def validate(self, data):
        if data.get("region") and data.get("city") and data["region"].name != data["city"].region.name:
            raise serializers.ValidationError("Selected city does not belong to the selected region.")
        return data


class AuditoriumSerializer(serializers.ModelSerializer):
    cinema_name = serializers.CharField(source='cinema.name', read_only=True)

    class Meta:
        model = Auditorium
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def validate_total_seats(self, value):
        if value <= 0:
            raise serializers.ValidationError("Total seats must be greater than 0.")
        return value

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Auditorium name cannot be empty.")
        return value

    def validate(self, data):
        # Optional: Avoid duplicate auditorium names per cinema
        cinema = data.get("cinema")
        name = data.get("name")
        if self.instance is None and Auditorium.objects.filter(cinema=cinema, name=name).exists():
            raise serializers.ValidationError("An auditorium with this name already exists in this cinema.")
        return data
