from django import forms

class EventForm(forms.Form):
    date = forms.DateTimeField()
    title = forms.CharField(
        max_length=225,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter event title here."
        })
    )
