from django import forms
from .models import Account


class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'surname',
            'firstname',
            'username',
            'trade_name',
            'email',
            'phone_number',
            'password',
            'd_o_b',
            'gender',
            'state_of_origin',
            'residential_address',
            'nationality',
            'recovery_question',
            'recovery_answer',
            'national_identifier',
            'biography',
            'other_link',
            'image_url'
        ]
