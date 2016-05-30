from django import forms
from .models import Lunchrequest
from bootstrap3_datetime.widgets import DateTimePicker

class LunchRequestForm(forms.ModelForm):
    class Meta:
        model = Lunchrequest
        fields = ('user', 'place', 'time', 'email')
        widgets = {
            'user': forms.TextInput(attrs={'class': 'textinput'}),
            'place': forms.TextInput(attrs={'class': 'textinput'}),
            'email': forms.TextInput(attrs={'class': 'textinput'}),

            'time': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False},
                    attrs={"id": "datetimewidget"})
        }
