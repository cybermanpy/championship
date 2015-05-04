from django.db import models
from events.models import Event

class Team(models.Model):
	description = models.CharField(blank=False, max_length=50)
	score = models.IntegerField(blank=True, default="0")
	gf = models.IntegerField(blank=False, default="0")
	gc = models.IntegerField(blank=False, default="0")
	pj = models.IntegerField(blank=False, default="0")
	pg = models.IntegerField(blank=False, default="0")
	pe = models.IntegerField(blank=False, default="0")
	pp = models.IntegerField(blank=False, default="0")
	fkevent = models.ForeignKey(Event)
	class Meta:
	    verbose_name = 'Team'
	    verbose_name_plural = 'Teams'
	def __unicode__(self):
		return '%s - %s' %(self.description,self.fkevent)