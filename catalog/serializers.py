from rest_framework import serializers
from .models import Book, Author, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "bio"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.name", read_only=True)
    category_names = serializers.StringRelatedField(
        source="categories", many=True, read_only=True
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "author_name",
            "categories",
            "category_names",
            "description",
            "published_date",
            "isbn",
            "cover_image_url",
            "created_at",
        ]