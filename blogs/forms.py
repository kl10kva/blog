from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Информация о пользователе"""
    class Meta:
        model = Post
        fields = [
            'title', 'description'
        ]

