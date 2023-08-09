from datetime import datetime

from django import forms
from .models import Tag, Author, Quote


class TagForm(forms.ModelForm):
    
    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
        widgets = {
            "born_date": forms.DateInput(attrs={"type": "date", 'max': datetime.now().date()})
        }


class QuoteForm(forms.ModelForm):
    
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple,
    )
    
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']