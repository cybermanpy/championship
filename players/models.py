from django.db import models
from teams.models import Team

class Player(models.Model):
	name = models.CharField(blank=False, max_length=50)
	goals = models.IntegerField(blank=False, default="0")
	fkteam = models.ForeignKey(Team)
	cedula = models.IntegerField(blank=False)
	agent = models.BooleanField(blank=False, default=False)
	subagent = models.BooleanField(blank=False, default=False)
	captain = models.BooleanField(blank=False, default=False)
	class Meta:
	    verbose_name = 'Player'
	    verbose_name_plural = 'Players'
	def __unicode__(self):
		return "%s - %s" %(self.name, self.fkteam)