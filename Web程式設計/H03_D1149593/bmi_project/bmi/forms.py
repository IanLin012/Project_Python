from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'height', 'weight']
        labels = {
            'name': 'Name',
            'height': 'Height(cm)',
            'weight': 'Weight(kg)',
        }

def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['height'].validators.append(
            forms.validators.MinValueValidator(140)
        )
        self.fields['height'].validators.append(
            forms.validators.MaxValueValidator(200)
        )
        self.fields['weight'].validators.append(
            forms.validators.MinValueValidator(30)
        )
        self.fields['weight'].validators.append(
            forms.validators.MaxValueValidator(120)
        )