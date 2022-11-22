from django import forms
from gamingdistribution.models import Game,Publisher

class GameForms(forms.ModelForm):
    class Meta:
        model=Game
        fields="__all__"

class PublisherForms(forms.ModelForm):
    class Meta:
        model=Publisher
        fields="__all__"