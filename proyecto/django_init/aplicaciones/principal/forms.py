from django import forms
from .models import persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = persona
        fields = "__all__"