from django import forms
from .models import Contact


class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': ''})
        # }
