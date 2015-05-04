from django.db import models
from fixtures.models import Fixture
from teams.models import Team
from results.models import Result

class Match(models.Model):
	fkhome = models.ForeignKey(Team, related_name='+')
	fkaway = models.ForeignKey(Team, related_name='+')
	fkresult = models.ForeignKey(Result)
	fkfixture = models.ForeignKey(Fixture)
	goalshome = models.IntegerField(blank=False, default="0")
	goalsaway = models.IntegerField(blank=False, default="0")
	class Meta:
	    verbose_name = 'Match'
	    verbose_name_plural = 'Matches'
	def __unicode__(self):
		return '%s - %s vs %s' %(self.fkfixture, self.fkhome, self.fkaway)