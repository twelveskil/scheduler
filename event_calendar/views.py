# pylint: disable=E0611
from django.shortcuts import render, HttpResponseRedirect
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
    # ISSUE AREA #
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = Event(
                date = form.cleaned_data['date'],
                event = form.cleaned_data['event']
            )
            event.save()
        return HttpResponseRedirect('/thanks/')
    # END ISSUE AREA #
    context = {
        'form' : form
    }
    return render(request, "event_create.html", context)
