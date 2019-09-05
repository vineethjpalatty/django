from django.forms import ModelForm, Textarea, TextInput
from .models import Editorial

class EditorialForm(ModelForm):
    class Meta:
        model = Editorial
        fields=['Heading','Description']
        widgets = {'Heading': TextInput(attrs={'class': 'input','rows':20,'cols':40, 'placeholder': 'Heading' }), 'Description': Textarea(attrs={'class': 'input', 'placeholder': 'Description'})}