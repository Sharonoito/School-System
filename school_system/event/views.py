from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar

from .models import *
from .utils import Calendar
from .forms import EventRegistrationForm


class CalendarView(generic.ListView):
    model = Event
    template_name = 'Calendar/calendar.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        calendar = Calendar(d.year, d.month)
        html_calendar = calendar.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_calendar)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context
        
def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    form = EventRegistrationForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request,'Calendar/calendar.html', {'form': form}) 



def register_event(request):
    if request.method=="POST":
        form=EventRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)   
    else:
        form=EventRegistrationForm()
    return render(request,"Calendar/register_event.html",{"form":form})    

def event_list(request):
    events=Event.objects.all()
    return render(request,"Calendar/event_list.html",{"events":events})


#Updating events information
def edit_event(request,id):
    event=Event.objects.get(id=id)

    if request.method=="POST":
        form=EventRegistrationForm(request.POST,instance=event)

        if form.is_valid():
            form.save()

    else:
        form=EventRegistrationForm(instance=event)
    return render (request,"Calendar/edit_event.html",{"form":form})


def event_profile(request,id):
    event=Event.objects.get(id=id)
    return render(request,"Calendar/event_profile.html",{"event":event})            


def delete_event(request,id):
    event=Event.objects.get(id=id)
    event.delete()
    return redirect("Calendar/event_list")            

