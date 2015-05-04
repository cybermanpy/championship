from django.db import models
from events.models import Event

class Image(models.Model):
	title = models.CharField(max_length=140)
	imagesource = models.ImageField(upload_to='championship/media/pic')
	fkevent = models.ForeignKey(Event)

	def __unicode__(self):
		return "%s" %(self.title)