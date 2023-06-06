from django import forms
from .models import Tag, Author, Quote


class TagForm(forms.ModelForm):
    name = forms.CharField(min_length=2, max_length=25, required=True, widget=forms.TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']
