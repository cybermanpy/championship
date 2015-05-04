from django.template.context import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseNotFound
from events.models import Event
from teams.models import Team

def viewStandings(request, id_event):
	get_event = Event.objects.get(id=id_event)
	request.session['title'] = get_event.name
	title = request.session['title']
	listTeam = Team.objects.filter(fkevent__id__exact=id_event).order_by('-score','-gf','gc')
	return render_to_response('viewstandings.html', {'listTeam':listTeam, 'title':title, 'id_event':id_event}, context_instance=RequestContext(request))