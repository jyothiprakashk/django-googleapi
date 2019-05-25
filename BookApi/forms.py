from django.forms import ModelForm, TextInput
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name']
        widgets = {'name' : TextInput (
            attrs={'class' : 'input', 'placeholder': 'Search and Add Your Book',}
        )}