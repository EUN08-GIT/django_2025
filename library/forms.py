from django import forms
from library.models import Book


class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title','content','uploaded_img']