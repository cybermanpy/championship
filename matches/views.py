from django.template.context import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from matches.models import Match
from events.models import Event

def viewFixture(request, id_event):
    fixture = Match.objects.filter(fkhome__fkevent__exact=id_event).order_by('id')
    title  = getTitle(id_event)
    return render_to_response('fixture.html', {'fixture':fixture, 'title':title, 'id_event':id_event}, context_instance=RequestContext(request))

def getTitle(id_event):
    listEvent = Event.objects.get(id=id_event)
    tmpTitle = listEvent.name
    return tmpTitle
