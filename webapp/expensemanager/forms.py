from django.forms import ModelForm
from .models import table

class ContactForm(ModelForm):
    class Meta:
        model=table
        fields=['cost','CATEGORY',]
