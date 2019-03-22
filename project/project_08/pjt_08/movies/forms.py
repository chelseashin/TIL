from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Movie, Score


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        
        
class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['score', 'content']
        widgets = {
            'score' : forms.NumberInput(attrs={
                'min' : '0',
                'max' : '5',
            })
        }