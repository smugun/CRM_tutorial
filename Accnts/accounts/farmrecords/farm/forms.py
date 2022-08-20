from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={
                                   'class': 'forms-control',
                                   'placeholder': 'Username'
                               }))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'forms-control',
                                   'placeholder': 'Password'
                               }))
    email = forms.CharField(max_length=100,
                            widget=forms.EmailInput(attrs={
                                'class': 'forms-control',
                                'placeholder': 'Email'
                            }))
    phone = forms.CharField(max_length=100,
                            widget=forms.NumberInput(attrs={
                                'class': 'forms-control',
                                'placeholder': 'phone'
                            }))
