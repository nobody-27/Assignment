from rest_framework import serializers
from books_app.models import Book

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','author','published_date')


class Videoserializer(serializers.Serializer):
    images = serializers.ImageField()
    
