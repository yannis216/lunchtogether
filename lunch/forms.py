from django import forms
from .models import Lunchrequest
from bootstrap3_datetime.widgets import DateTimePicker

class LunchRequestForm(forms.ModelForm):
    class Meta:
        model = Lunchrequest
        fields = ('user', 'email', 'university', 'yoursubject', 'spokenlanguages', 'aboutyou', 'lunchpreference')
        widgets = {
            'user': forms.TextInput(attrs={'class': 'textinput'}),
            #'place': forms.TextInput(attrs={'class': 'textinput'}),
            'email': forms.TextInput(attrs={'class': 'textinput'}),
            'university': forms.TextInput(attrs={'class': 'textinput'}),
            'yoursubject': forms.TextInput(attrs={'class': 'textinput'}),
            'spokenlanguages': forms.TextInput(attrs={'class': 'textinput'}),
            'aboutyou': forms.TextInput(attrs={'class': 'textinput'}),
            'lunchpreference': forms.TextInput(attrs={'class': 'textinput'}),

            #'time': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False},
                    #attrs={"id": "datetimewidget"})
        }
