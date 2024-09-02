from django import forms

class EmailVerifyForm(forms.Form):
    email = forms.EmailField(label="Email Address", max_length=254)

