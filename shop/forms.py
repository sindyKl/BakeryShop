from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={
        'name': 'name',
        'placeholder': 'Name',
        'class': 'name mr-3 mb-3'
    }))
    email = forms.EmailField(label='', required=True, widget=forms.EmailInput(attrs={
        'name': 'email',
        'placeholder': 'E-mail',
        'class': 'mb-3'
    }))
    subject = forms.CharField(label='', max_length=250, widget=forms.TextInput(attrs={
        'placeholder': 'Subject',
        'class': 'mb-3'
    }))
    message = forms.CharField(label='', required=True, widget=forms.Textarea(attrs={
        'name': 'message',
        'placeholder': 'Message',
        'style': 'height: 150px;'
    }))