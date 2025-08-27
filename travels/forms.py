from django import forms
from .models import TravelOption
from django.utils import timezone

class TravelSearchForm(forms.Form):
    type = forms.ChoiceField(choices=[('', 'All')] + list(TravelOption.TRAVEL_TYPES), required=False)
    source = forms.CharField(required=False)
    destination = forms.CharField(required=False)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))


class TravelOptionForm(forms.ModelForm):
    class Meta:
        model = TravelOption
        fields = ['type', 'source', 'destination', 'date_time', 'price', 'available_seats']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'available_seats': forms.NumberInput(attrs={'min': '0'}),
        }
    
    def clean_date_time(self):
        date_time = self.cleaned_data.get('date_time')
        if date_time and date_time < timezone.now():
            raise forms.ValidationError("Date and time cannot be in the past!")
        return date_time