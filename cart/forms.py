from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 31)]

class CartAddProductForm(forms.Form):
    
    quantity = forms.TypedChoiceField(label='', choices=PRODUCT_QUANTITY_CHOICES, coerce=int, widget=forms.NumberInput(attrs={
        'id': 'qty',
        'class': 'input-text qty text',
        'size': '4',
        'name': 'quantity',
        'min': '1',
        'max': '30',
        'step': '1',
        'value': '1',
    }))

    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

