from rest_framework import serializers
from .models import Author,Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','price']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['id','name','books']

    def create(self,validated_data):
        books_data = validated_data.pop('books')
        author = Author.objects.create(**validated_data)

        for book in books_data:
            Book.objects.create(author=author, **book)

        return author
    
    def update(self,instance,validated_data):
        books_data = validated_data.pop('books')
        instance.name = validated_data.get('name',instance.name)
        instance.save()

        instance.books.all().delete()

        for book in books_data:
            Book.objects.create(author=instance, **book)

        return instance