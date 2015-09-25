from django import forms
from tracker.models import Tracker

class TrackerForm(forms.ModelForm):

    ip = forms.GenericIPAddressField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ip Address'}),
                                     error_messages={'required': 'Ip is required.'})
    port = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Port'}),
                              error_messages={'required': 'Port is required.'})
    OPTIONS = (
            (30, "30fps"),
            (60, "60fps"),
            )
    frame_rate = forms.ChoiceField(choices=OPTIONS, widget=forms.Select(attrs= {'class':'form-control'}),
                                   error_messages={'required': 'Frame rate is required.'})

    class Meta:
        model = Tracker
        exclude = ()

class RecordForm(forms.ModelForm):

    time = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required': 'Time is required'})

    class Meta:
        model = Tracker
        fields = ('time',)