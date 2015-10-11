from django.template.context import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from events.models import Event

def index(request):
    title = 'Torneos'
    listEvent = Event.objects.filter(status=True).order_by('-id')
    return render_to_response('viewevents.html',{'title':title, 'listEvent':listEvent}, context_instance=RequestContext(request))
