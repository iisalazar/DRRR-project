from django import forms
from .models import Content

class ContentCreateForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('header', 'body')
        widgets = {
            'header': forms.TextInput(),
            'body' : forms.Textarea()
        }