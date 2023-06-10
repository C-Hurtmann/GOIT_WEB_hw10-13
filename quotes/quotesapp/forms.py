from django import forms
from .models import Tag, Author, Quote


class TagForm(forms.ModelForm):
    name = forms.CharField(min_length=2, max_length=25, required=True, widget=forms.TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(forms.ModelForm):
    fullname = forms.CharField(min_length=2, max_length=50, required=True, widget=forms.TextInput())
    born_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    born_location = forms.CharField(min_length=2, max_length=50 ,widget=forms.TextInput())
    description = forms.Textarea()
    
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(forms.ModelForm):
    quote = forms.Textarea()
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    
    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']