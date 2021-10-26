from django import forms
from django.db import models
from django.forms import fields
from .models import Posts



class PostsModelForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = [ 'author_name',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'active': forms.Select(attrs={'class': ''}),
        }
    def clean_title(self):
        title=self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('Please add Title')
        return title
    def clean_content(self):
        content=self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError('Please add some content')
        return content