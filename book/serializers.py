from rest_framework import serializers
from .models import *


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    character = CharacterSerializer(many=True)
    author = AuthorSerializer(many=True)
    # character = CharacterSerializer(many=False)
    class Meta:
        model = Book
        fields = '__all__'

class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']