from django import forms
from .models import Article


class ArticleCreationForm(forms.ModelForm):
    title = forms.CharField(label="",
                            widget=forms.TextInput(attrs={'placeholder': 'Your title'}))

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]
