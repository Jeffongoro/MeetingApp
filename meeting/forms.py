from django import forms
from django.forms import ModelForm
from .models import Meeting


class MeetingForm(ModelForm):
    minutes = forms.CharField(required=False)
    attachments = forms.FileField(required=False)

    class Meta:
        model = Meeting
        fields = ('title', 'agenda','venue', 'guests', 'start_time', 'end_time', 'minutes', 'attachments')
        widgets = {
          'title': forms.TextInput( attrs={ 'class':'form-control'}),
          'agenda': forms.TextInput( attrs={ 'class':'form-control'}),
          'venue': forms.TextInput( attrs={ 'class':'form-control'}),
          'guests': forms.TextInput( attrs={ 'class':'form-control'}),
          #'minutes'=forms.CharField(widget=forms.Textarea(attrs={'class':'comment','title':'add comment'}))
          'start_time': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local', 'class':'form-control'}),
          'end_time': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local', 'class':'form-control'}),
        }



