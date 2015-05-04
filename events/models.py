from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
	name = models.CharField(blank=False, max_length=50)
	fkusr = models.ForeignKey(User)
	description = models.CharField(blank=True, max_length=140)
	status = models.BooleanField(blank=False, default=False)
	imagesource = models.ImageField(upload_to='championship/media/event')
	class Meta:
	    verbose_name = 'Event'
	    verbose_name_plural = 'Events'
	def __unicode__(self):
		return self.name