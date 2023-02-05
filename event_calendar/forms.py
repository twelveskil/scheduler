from django import forms

class EventForm(forms.Form):
    date = forms.CharField(
        max_length=225,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Date: YYYY-MM-DD"
        })
    )
    event = forms.CharField(
        max_length=225,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter event name here."
        })
    )
    