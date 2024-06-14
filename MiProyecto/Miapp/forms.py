from django import forms
from .models import Author, Book, Review

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'review_text', 'rating']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search for a book', max_length=100)
