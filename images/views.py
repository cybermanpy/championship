from django.template.context import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseNotFound
from images.models import Image

def viewImage(request, id_event):
	listImage = Image.objects.filter(fkevent__id__exact=id_event)
	title = request.session['title']
	return render_to_response('viewimages.html', {'listImage':listImage, 'title':title, 'id_event':id_event}, context_instance=RequestContext(request))