from django.template.context import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseNotFound
from events.models import Event
from teams.models import Team
from players.models import Player
from matches.views import getTitle

def viewStandings(request, id_event): 
    listTeam = Team.objects.filter(fkevent__id__exact=id_event).order_by('-score','-gf','gc')
    title = getTitle(id_event)
    return render_to_response('viewstandings.html', {'listTeam':listTeam, 'title':title, 'id_event':id_event}, context_instance=RequestContext(request))

def viewTeams(request, id_event):
    listTeam = Player.objects.filter(fkteam__fkevent__id__exact=id_event).order_by('fkteam') 
    title = getTitle(id_event)
    return render_to_response('viewsteams.html', {'listTeam':listTeam, 'title':title, 'id_event':id_event}, context_instance=RequestContext(request))
