from django.template.context import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from matches.models import Match

def viewFixture(request, id_event):
    fixture = Match.objects.filter(fkhome__fkevent__exact=id_event).order_by('id')
    title = request.session['title']
    return render_to_response('fixture.html', {'fixture':fixture, 'title':title, 'id_event':id_event}, context_instance=RequestContext(request))
