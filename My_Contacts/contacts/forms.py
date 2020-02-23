from django import forms
from .models import Contacts

class AddContacts(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('name','email','phone','info','gender','image')
        # labels = {
        # }