from django.forms import ModelForm, CharField, TextInput
from . import models


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput)
    
    class Meta:
        model = models.Tag
        fields = ['name']