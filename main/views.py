from django.shortcuts import render, redirect
from main.forms import MoodEntryForm
from main.models import MoodEntry
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306152494',
        'name': 'Andrew Devito Aryo',
        'class': 'PBP F',
        'mood_entries': MoodEntry.objects.all()
    }

    return render(request, "main.html", context)

def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)

def show_xml(_):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json(_):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_xml_by_id(_, id):
    data = MoodEntry.objects.filter(id=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json_by_id(_, id):
    data = MoodEntry.objects.filter(id=id)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')