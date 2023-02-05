# pylint: disable=E0611
from django.shortcuts import render
from event_calendar.models import Event
from event_calendar.forms import EventForm

def calendar_index(request):
    events = Event.objects.all()
    context = {
        "events" : events,
    }
    return render(request, "calendar_index.html", context)

def event_create(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = Event(
                date = form.cleaned_data['date'],
                title = form.cleaned_data['title']
            )
            event.save()
    context = {
        'form' : form
    }
    return render(request, "event_create.html", context)
