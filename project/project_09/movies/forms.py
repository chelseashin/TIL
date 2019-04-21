from django import forms
from .models import Score

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('content', 'value', )
        widgets = {
            'value' : forms.NumberInput(attrs={
                'min' : '0',
                'max' : '5',
            })
        }