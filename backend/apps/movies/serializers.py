from rest_framework import serializers
from .models import *
from datetime import date
from apps.seats.serializers import *
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ['id', 'name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'code']
class SubtitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtitle
        fields = ['id', 'language']
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ['id', 'name', 'year', 'category']
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'created_at']
        read_only_fields = ['user', 'created_at']

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    formats = FormatSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    subtitles = SubtitleSerializer(many=True, read_only=True)
    country = CountrySerializer(read_only=True)
    awards = AwardSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    genre_ids = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True, write_only=True, source='genres')
    format_ids = serializers.PrimaryKeyRelatedField(queryset=Format.objects.all(), many=True, write_only=True, source='formats')
    tag_ids = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, write_only=True, source='tags')
    subtitle_ids = serializers.PrimaryKeyRelatedField(queryset=Subtitle.objects.all(), many=True, write_only=True, source='subtitles')
    country_id = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), write_only=True, source='country')

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'synopsis',
            'duration_minutes',
            'classification',
            'poster',
            'trailer_url',
            'director',
            'main_cast',
            'production_company',
            'original_language',
            'expected_audience',
            'is_scheduled',
            'release_date',
            'genres',
            'formats',
            'tags',
            'subtitles',
            'country',
            'awards',
            'likes_count',
            'genre_ids',
            'format_ids',
            'tag_ids',
            'subtitle_ids',
            'country_id',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def validate(self, attrs):
        if attrs.get('duration_minutes', 0) < 30:
            raise serializers.ValidationError({
                "duration_minutes": "La duración mínima debe ser de 30 minutos."
            })

        release_date = attrs.get('release_date')
        if release_date and release_date > date.today().replace(year=date.today().year + 5):
            raise serializers.ValidationError({
                "release_date": "La fecha de estreno es demasiado lejana."
            })

        trailer = attrs.get('trailer_url', '')
        if trailer and not ('youtube.com' in trailer or 'vimeo.com' in trailer):
            raise serializers.ValidationError({
                "trailer_url": "El trailer debe ser un enlace de YouTube o Vimeo."
            })

        return attrs

    def create(self, validated_data):
        genres = validated_data.pop('genres', [])
        formats = validated_data.pop('formats', [])
        tags = validated_data.pop('tags', [])
        subtitles = validated_data.pop('subtitles', [])
        movie = super().create(validated_data)
        movie.genres.set(genres)
        movie.formats.set(formats)
        movie.tags.set(tags)
        movie.subtitles.set(subtitles)
        return movie

    def update(self, instance, validated_data):
        genres = validated_data.pop('genres', None)
        formats = validated_data.pop('formats', None)
        tags = validated_data.pop('tags', None)
        subtitles = validated_data.pop('subtitles', None)
        movie = super().update(instance, validated_data)
        if genres is not None:
            movie.genres.set(genres)
        if formats is not None:
            movie.formats.set(formats)
        if tags is not None:
            movie.tags.set(tags)
        if subtitles is not None:
            movie.subtitles.set(subtitles)
        return movie


class ShowTimeSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    room_name = serializers.CharField(source='room.name', read_only=True)
    format_name = serializers.CharField(source='format.name', read_only=True)

    class Meta:
        model = ShowTime
        fields = [
            'id',
            'movie', 'movie_title',
            'room', 'room_name',
            'format', 'format_name',
            'start_time', 'end_time',
            'price',
            'is_active'
        ]

    def validate(self, data):
        room = data.get('room')
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if ShowTime.objects.filter(room=room, start_time__lt=end_time, end_time__gt=start_time).exists():
            raise serializers.ValidationError("Ya existe una función en esa sala y horario.")
        return data
