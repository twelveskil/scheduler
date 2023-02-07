# pylint: disable=E0611
from django.shortcuts import render, redirect
from event_calendar.models import Event
from event_calendar.forms import EventForm

def calendar_index(request):
    events = Event.objects.all().order_by('date')
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
            return redirect('calendar_index')
    context = {
        'form' : form
    }
    return render(request, "event_create.html", context)

def event_edit(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        form = EventForm(request.POST or None)
        if form.is_valid():
            event.title = form.cleaned_data['title']
            event.date = form.cleaned_data['date']
            event.save()
            return redirect("calendar_index")
    else:
        form = EventForm(initial={
            'title': event.title,
            'date': event.date
        })
    context = {
        "event" : event,
        "form" : form
    }
    return render(request, 'event_edit.html', context)

def event_delete(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return redirect('calendar_index')
