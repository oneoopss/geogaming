# forms.py
from django import forms
from .models import Event, AvatarProfile

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'is_public']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите название события'}),
            'description': forms.Textarea(attrs={'placeholder': 'Что нового?'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'custom-checkbox'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = AvatarProfile
        fields = ['profile_picture']