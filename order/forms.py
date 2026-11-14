from django import forms
from .models import Address

class AddForm(forms.ModelForm):
    class Meta:
        model=Address
        # fields='__all__'
        exclude=['user']