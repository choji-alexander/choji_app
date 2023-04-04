from django import forms
from .models import Product


class ProductAdditionForm(forms.ModelForm):
    title = forms.CharField(label="",
                            widget=forms.TextInput(attrs={'placeholder': 'Your title'}))

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
