from django import forms
from .models import xam
class xamform(forms.ModelForm):
    class Meta:
        model=xam
        fields= '__all__'