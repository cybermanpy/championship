from django.db import models
from players.models import Player
from fixtures.models import Fixture

class Card(models.Model):
	description = models.CharField(blank=False, max_length=50)
	cards = models.ManyToManyField(Player, through='CardPlayer')
	class Meta:
	    verbose_name = 'Card'
	    verbose_name_plural = 'Cards'
	def __unicode__(self):
		return self.description

class CardPlayer(models.Model):
	fkcard = models.ForeignKey(Card)
	fkfixture = models.ForeignKey(Fixture)
	fkplayer = models.ForeignKey(Player)
	class Meta:
	    verbose_name = 'CardAndPlayer'
	    verbose_name_plural = 'CardAndPlayers'
	def __unicode__(self):
		return '%s %s %s' %(self.fkcard, self.fkfixture, self.fkplayer)