from django import forms
from .models import Blog, Comment

class Formblog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']