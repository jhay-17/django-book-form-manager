from django import forms
from crudapp.models import Book
from django.forms import fields

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = "__all__"
        fields = ['isbn', 'name', 'author', 'category']
        labels = {
            'isbn': 'Book ISBN',
            'name': 'Book Name',
            'author': 'Author',
            'category': 'Book Category',
        } 
        widgets = {
            'isbn': forms.TextInput(attrs={
                'placeholder': "Enter the book's ISBN", 
                'class': 'border rounded p-2 placeholder-gray-500 text-sm'  # Adjusts placeholder text size
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter the book name', 
                'class': 'border rounded p-2 placeholder-gray-500 text-sm'
            }),
            'author': forms.TextInput(attrs={
                'placeholder': 'Enter the author name', 
                'class': 'border rounded p-2 placeholder-gray-500 text-sm'
            }),
            'category': forms.TextInput(attrs={
                'placeholder': 'Enter the book category', 
                'class': 'border rounded p-2 placeholder-gray-500 text-sm'
            }),
        }
