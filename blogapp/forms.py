from django import forms
from .models import Blog_model


class BlogPost(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={'class': 'modelform-input', 'rows': 1}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'modelform-input'}))
    class Meta:
        model = Blog_model
        fields = ['title', 'img', 'body',]