from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'your username'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'your password'}))


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'your username'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'your password'}))
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'your email'}))
