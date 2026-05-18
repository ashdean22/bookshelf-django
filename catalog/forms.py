from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "categories",
            "description",
            "published_date",
            "isbn",
            "cover_image_url",
        ]
        widgets = {
            "published_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }