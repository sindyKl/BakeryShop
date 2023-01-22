from django import forms
from .models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'name': 'name', 'placeholder': 'Name', 'class': 'mb-3'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'name': 'email', 'placeholder': 'E-mail', 'class': 'mb-3'}))
    phone = PhoneNumberField(label='Choose your country code', widget=PhoneNumberPrefixWidget(attrs={'name': 'telephone', 'placeholder': 'Phone number', 'class': 'mb-3'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'name': 'password1', 'placeholder': 'Password', 'class': 'mb-3'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'name': 'password2', 'placeholder': 'Confirm password', 'class': 'mb-3'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('email', 'password')
        

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'bio', 'instagram', 'image')        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',             
            }),
            'bio': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'instagram': forms.TextInput(attrs={
                'class': 'form-control',                
            }),
            'image': forms.FileInput(attrs={
                'accept': 'image/*',
            })
        }
        

class ChangePassswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'name': 'password',
        'placeholder': 'Old password',
        'class': 'mb-3',
        'autofocus': True,
        }))
    new_password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'name': 'password1',
        'placeholder': 'Password',
        'class': 'mb-3'
        }))
    new_password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'name': 'password2',
        'placeholder': 'Confirm password',
        'class': 'mb-3'
        }))
