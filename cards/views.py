from django.template.context import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseNotFound
from cards.models import CardPlayer
from matches.views import getTitle

def viewCards(request, id_event):
    listCards = CardPlayer.objects.filter(fkplayer__fkteam__fkevent__id=id_event).order_by('-fkfixture')
    title = getTitle(id_event)
    return render_to_response('viewcards.html', {'listCards':listCards, 'title':title, 'id_event':id_event}, context_instance=RequestContext(request))
