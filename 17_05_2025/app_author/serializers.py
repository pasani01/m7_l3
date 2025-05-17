from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Author
from datetime import date


class AuthorCreateSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'brith_date', 'books_count', 'biography']
        read_only_fields = ['id', 'slug']
        
    def validate_brith_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Birth date cannot be in the future.")
        return value

    

class AuthorListSerializer(ModelSerializer):
    link=SerializerMethodField('get_link')

    class Meta:
        model = Author
        fields = ['name', 'brith_date', 'books_count', 'biography','link']
        read_only_fields = ['id', 'slug']

    def get_link(self, obj):
        return f'http://127.0.0.1:8000/api/authors/{obj.slug}/'
    


class AuthorDetailSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'brith_date', 'books_count', 'biography',]
        read_only_fields = ['id', 'slug',]
    
