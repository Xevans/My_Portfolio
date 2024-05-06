from django import forms

class NameForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)