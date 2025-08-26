from django import forms
from .models import TravelOption

class TravelSearchForm(forms.Form):
    type = forms.ChoiceField(choices=[('', 'All')] + list(TravelOption.TRAVEL_TYPES), required=False)
    source = forms.CharField(required=False)
    destination = forms.CharField(required=False)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
