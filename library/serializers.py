from rest_framework import serializers
from .models import Author, Book, Borrow

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')
    class Meta:
        model = Book
        fields = '__all__'

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ('book',)

class BorrowListSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title')
    author_name = serializers.CharField(source='book.author.name')
    class Meta:
        model = Borrow
        fields = '__all__'