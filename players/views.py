from django.template.context import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from players.models import Player

def viewPlayesGoals(request, id_event):
    listPlayer = Player.objects.filter(fkteam__fkevent__id__exact=id_event).order_by('-goals').exclude(goals=0)
    title = request.session['title']
    return render_to_response('viewplayers.html', {'listPlayer':listPlayer, 'title':title, 'id_event':id_event}, context_instance=RequestContext(request))
